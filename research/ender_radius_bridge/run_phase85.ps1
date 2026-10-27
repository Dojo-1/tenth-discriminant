param([ValidateSet('run')][string]$Mode)
$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$taskPrevious = @(Get-ChildItem $PSScriptRoot -Filter "PHASE85_${Mode}_*.result.json" | ForEach-Object { Get-Content $_.FullName -Raw | ConvertFrom-Json })
$taskSpent = ($taskPrevious | Measure-Object elapsed_seconds -Sum).Sum
if ($null -eq $taskSpent) { $taskSpent = 0 }
$taskLimit = 120
if ($taskPrevious.Count -ge 1) { throw 'Phase85 one-shot run already invoked; no rerun' }
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
$taskPrefix = Join-Path $PSScriptRoot "PHASE85_${Mode}_$taskStamp"
$taskExe = (Get-Command python).Source
$taskArgs = @('research/ender_radius_bridge/Phase85Feasibility.py')
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'Phase85Feasibility.py') -Destination "$taskPrefix.source.py"
$taskSourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath "$taskPrefix.source.py").Hash.ToLowerInvariant()
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskExe -WorkingDirectory $taskRepo -WindowStyle Hidden -PassThru -ArgumentList $taskArgs -RedirectStandardOutput "$taskPrefix.stdout.log" -RedirectStandardError "$taskPrefix.stderr.log"
$taskHandle = $taskRun.Handle
$taskOwned = [System.Collections.Generic.HashSet[int]]::new()
[void]$taskOwned.Add($taskRun.Id)
$taskPeak = 0L
$taskReason = ''
while (-not $taskRun.HasExited) {
    $taskProcesses = @(Get-CimInstance Win32_Process -Filter "Name='python.exe'")
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
if (-not $taskReason -and (Select-String -LiteralPath "$taskPrefix.stdout.log" -Pattern 'maximum number of heartbeats|maximum recursion depth|deterministic.*timeout' -Quiet)) { $taskReason = 'lean_internal_resource_limit' }
$taskResult = [ordered]@{phase=85;mode=$Mode;scope='Sealed scalar feasibility of conservative normalized h<=2 loss; not a cutoff';source_sha256=$taskSourceHash;source_snapshot=[IO.Path]::GetFileName("$taskPrefix.source.py");attempt=$taskPrevious.Count+1;exit_code=$taskCode;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;cumulative_before_seconds=$taskSpent;time_limit_seconds=$taskLimit;memory_threshold_mb=8192;observed_peak_working_set_bytes=$taskPeak;stop_reason=$taskReason;executable=$taskExe;arguments=$taskArgs;stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log");stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")}
$taskResult | ConvertTo-Json -Depth 5 | Set-Content "$taskPrefix.result.json" -Encoding utf8
Get-Content "$taskPrefix.stdout.log" -Tail 35
Get-Content "$taskPrefix.stderr.log" -Tail 20
$taskResult | ConvertTo-Json -Depth 5
exit $taskCode
