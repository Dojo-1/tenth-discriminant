param([ValidateSet('pilot','build','root','input','audit')][string]$Mode)
$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$taskPrevious = @(Get-ChildItem $PSScriptRoot -Filter "PHASE41_${Mode}_*.result.json" | ForEach-Object { Get-Content $_.FullName -Raw | ConvertFrom-Json })
if ($Mode -eq 'pilot' -and $taskPrevious.Count) { throw 'Exactly one Phase41 pilot; no rerun' }
$taskSpent = ($taskPrevious | Measure-Object elapsed_seconds -Sum).Sum
if ($null -eq $taskSpent) { $taskSpent = 0 }
$taskLimit = switch ($Mode) { 'pilot' {120}; 'build' {[Math]::Min(600,[Math]::Floor(900-$taskSpent))}; 'root' {1200}; default {180} }
if ($Mode -eq 'build' -and ($taskPrevious.Count -ge 4 -or @($taskPrevious | Where-Object stop_reason).Count -or $taskLimit -le 0)) { throw 'Phase41 proof-attempt budget exhausted or resource stop' }
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
$taskPrefix = Join-Path $PSScriptRoot "PHASE41_${Mode}_$taskStamp"
$taskExe = (Get-Command lake.exe).Source
$taskDir = Join-Path $taskRepo 'lean'
$taskArgs = switch ($Mode) {
    'pilot' { @((Join-Path $PSScriptRoot 'phase41_aspect_pilot.py')) }
    'build' { @('build','TenthDiscriminant.AspectRatioLowerEnvelope') }
    'root' { @('build') }
    'input' { @('env','lean','-j','1','../research/ender_radius_bridge/Phase41InputCheck.lean') }
    'audit' { @('env','lean','-j','1','Audit.lean') }
}
if ($Mode -eq 'pilot') { $taskExe = (Resolve-Path (Join-Path $taskRepo '../numeric-env/Scripts/python.exe')).Path }
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskExe -WorkingDirectory $taskDir -WindowStyle Hidden -PassThru -ArgumentList $taskArgs -RedirectStandardOutput "$taskPrefix.stdout.log" -RedirectStandardError "$taskPrefix.stderr.log"
$taskHandle = $taskRun.Handle
$taskOwned = [System.Collections.Generic.HashSet[int]]::new()
[void]$taskOwned.Add($taskRun.Id)
$taskPeak = 0L
$taskReason = ''
while (-not $taskRun.HasExited) {
    $taskProcesses = @(Get-CimInstance Win32_Process -Filter "Name='lake.exe' OR Name='lean.exe' OR Name='elan.exe' OR Name='python.exe'")
    do {
        $taskAdded = $false
        foreach ($taskProcess in $taskProcesses) {
            if ($taskOwned.Contains([int]$taskProcess.ParentProcessId)) {
                if ($taskOwned.Add([int]$taskProcess.ProcessId)) { $taskAdded = $true }
            }
        }
    } while ($taskAdded)
    foreach ($taskProcess in $taskProcesses) {
        if ($taskOwned.Contains([int]$taskProcess.ProcessId)) {
            $taskMetric = Get-Process -Id $taskProcess.ProcessId -ErrorAction SilentlyContinue
            if ($taskMetric) {
                $taskPeak = [Math]::Max($taskPeak,$taskMetric.WorkingSet64)
                if ($taskMetric.WorkingSet64 -gt 8192MB) { $taskReason = 'memory_limit' }
            }
        }
    }
    if (([DateTime]::UtcNow-$taskStart).TotalSeconds -gt $taskLimit) { $taskReason = 'time_limit' }
    if ($taskReason) {
        foreach ($taskProcess in $taskProcesses) {
            if ($taskOwned.Contains([int]$taskProcess.ProcessId)) { Stop-Process -Id $taskProcess.ProcessId -ErrorAction SilentlyContinue }
        }
    }
    Start-Sleep -Milliseconds 500
    $taskRun.Refresh()
}
$taskRun.WaitForExit()
$taskCode = if ($taskReason) {99} elseif ($null -eq $taskRun.ExitCode) {98} else {$taskRun.ExitCode}
$taskResult = [ordered]@{phase=41;mode=$Mode;scope='Preregistered aspect-ratio bridge or separately labelled verification';attempt=$taskPrevious.Count+1;exit_code=$taskCode;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;cumulative_before_seconds=$taskSpent;time_limit_seconds=$taskLimit;memory_threshold_mb=8192;observed_peak_working_set_bytes=$taskPeak;stop_reason=$taskReason;executable=$taskExe;arguments=$taskArgs;stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log");stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")}
$taskResult | ConvertTo-Json -Depth 5 | Set-Content "$taskPrefix.result.json" -Encoding utf8
Get-Content "$taskPrefix.stdout.log" -Tail 25
Get-Content "$taskPrefix.stderr.log" -Tail 20
$taskResult | ConvertTo-Json -Depth 5
exit $taskCode
