$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if (@(Get-ChildItem $PSScriptRoot -Filter 'PHASE112_synthetic_*').Count) { throw 'Phase112 one-shot synthetic validation already started' }
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
$taskPrefix = Join-Path $PSScriptRoot "PHASE112_synthetic_$taskStamp"
Copy-Item -LiteralPath (Join-Path $taskRepo 'lean/control_schedule.py') -Destination "$taskPrefix.controller.py"
Copy-Item -LiteralPath (Join-Path $taskRepo 'lean/control_schedule_tests.py') -Destination "$taskPrefix.tests.py"
$taskExe = (Get-Command python -CommandType Application | Select-Object -First 1).Source
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskExe -WorkingDirectory (Join-Path $taskRepo 'lean') -WindowStyle Hidden -PassThru -ArgumentList @('control_schedule_tests.py') -RedirectStandardOutput "$taskPrefix.stdout.log" -RedirectStandardError "$taskPrefix.stderr.log"
$taskHandle = $taskRun.Handle
$taskOwned = [System.Collections.Generic.HashSet[int]]::new()
[void]$taskOwned.Add($taskRun.Id)
$taskPeak = 0L
$taskReason = ''
while (-not $taskRun.HasExited) {
    $taskProcesses = @(Get-CimInstance Win32_Process -Filter "Name='python.exe' OR Name='python3.exe'")
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
    if (([DateTime]::UtcNow-$taskStart).TotalSeconds -gt 120) { $taskReason = 'time_limit' }
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
$taskResult = [ordered]@{phase=112;mode='synthetic';attempt=1;scope='Eight synthetic scheduler tests only; no Lean or real control family invoked';command=@($taskExe,'control_schedule_tests.py');cwd='lean';exit_code=$taskCode;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;time_limit_seconds=120;memory_threshold_mb=8192;observed_peak_working_set_bytes=$(if ($taskPeak) {$taskPeak} else {$null});memory_observation=$(if ($taskPeak) {'sampled per owned process'} else {'UNOBSERVED'});stop_reason=$taskReason;controller_snapshot=[IO.Path]::GetFileName("$taskPrefix.controller.py");tests_snapshot=[IO.Path]::GetFileName("$taskPrefix.tests.py");stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log");stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")}
$taskResult | ConvertTo-Json -Depth 5 | Set-Content "$taskPrefix.result.json" -Encoding utf8
Get-Content "$taskPrefix.stdout.log" -Tail 12
Get-Content "$taskPrefix.stderr.log" -Tail 20
$taskResult | ConvertTo-Json -Depth 5
exit $taskCode
