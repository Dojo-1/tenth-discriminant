$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if (@(Get-ChildItem $PSScriptRoot -Filter 'PHASE113_trial_*').Count) { throw 'Phase113 single execution already started' }
$taskPrefix = Join-Path $PSScriptRoot ('PHASE113_trial_'+[DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff'))
$taskSource = Join-Path $PSScriptRoot 'phase113_radial_blocks.py'
Copy-Item -LiteralPath $taskSource -Destination "$taskPrefix.source.py"
$taskExe = (Get-Command python -CommandType Application | Select-Object -First 1).Source
$taskArgs = @('research/ender_radius_bridge/phase113_radial_blocks.py','--output',"$taskPrefix.data.jsonl")
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskExe -WorkingDirectory $taskRepo -WindowStyle Hidden -PassThru -ArgumentList $taskArgs -RedirectStandardOutput "$taskPrefix.stdout.log" -RedirectStandardError "$taskPrefix.stderr.log"
$taskHandle = $taskRun.Handle
$taskOwned = [System.Collections.Generic.HashSet[int]]::new()
[void]$taskOwned.Add($taskRun.Id)
$taskPeak = 0L
$taskReason = ''
while (-not $taskRun.HasExited) {
    $taskProcesses = @(Get-CimInstance Win32_Process -Filter "Name='python.exe' OR Name='python3.exe' OR Name='git.exe'")
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
    if (([DateTime]::UtcNow-$taskStart).TotalSeconds -gt 180) { $taskReason = 'time_limit' }
    if ($taskReason) {
        foreach ($taskProcess in $taskProcesses) {
            if ($taskOwned.Contains([int]$taskProcess.ProcessId)) { Stop-Process -Id $taskProcess.ProcessId -ErrorAction SilentlyContinue }
        }
    }
    Start-Sleep -Milliseconds 500
    $taskRun.Refresh()
}
$taskRun.WaitForExit()
$taskCode = if ($taskReason) {99} elseif ($null -eq $taskRun.ExitCode) {100} else {$taskRun.ExitCode}
$taskResult = [ordered]@{phase=113;attempt=1;scope='Sealed full radial-block finite feasibility; no Lean';command=@($taskExe)+$taskArgs;cwd=$taskRepo;exit_code=$taskCode;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;time_limit_seconds=180;memory_threshold_mb=8192;observed_peak_working_set_bytes=$(if ($taskPeak) {$taskPeak} else {$null});stop_reason=$taskReason;source_snapshot=[IO.Path]::GetFileName("$taskPrefix.source.py");source_sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath "$taskPrefix.source.py").Hash.ToLowerInvariant();data=[IO.Path]::GetFileName("$taskPrefix.data.jsonl");stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log");stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")}
$taskResult | ConvertTo-Json -Depth 5 | Set-Content "$taskPrefix.result.json" -Encoding utf8
Get-Content "$taskPrefix.stdout.log" -Tail 30
Get-Content "$taskPrefix.stderr.log" -Tail 15
$taskResult | ConvertTo-Json -Depth 5
exit $taskCode
