param([int]$MemoryLimitMB = 8192)
$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
$taskLeanDir = Join-Path $taskRepo 'lean'
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmss')
$taskOut = Join-Path $PSScriptRoot "PHASE25_INTEGER_CHUNKS_$taskStamp.stdout.log"
$taskErr = Join-Path $PSScriptRoot "PHASE25_INTEGER_CHUNKS_$taskStamp.stderr.log"
$taskResult = Join-Path $PSScriptRoot "PHASE25_INTEGER_CHUNKS_$taskStamp.result.json"
$taskLake = (Get-Command lake.exe).Source
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskLake -WorkingDirectory $taskLeanDir -PassThru -WindowStyle Hidden `
    -ArgumentList @('env','lean','-j','1','-s','16384','--profile',
        '../research/ender_radius_bridge/FirstIntervalTableCheck.lean') `
    -RedirectStandardOutput $taskOut -RedirectStandardError $taskErr
$taskOwned = [System.Collections.Generic.HashSet[int]]::new()
[void]$taskOwned.Add($taskRun.Id)
$taskPeak = 0L
$taskStopped = $false
while (-not $taskRun.HasExited) {
    $taskProcesses = @(Get-CimInstance Win32_Process -Filter "Name='lake.exe' OR Name='lean.exe' OR Name='elan.exe'")
    do {
        $taskAdded = $false
        foreach ($taskProcess in $taskProcesses) {
            if ($taskOwned.Contains([int]$taskProcess.ParentProcessId)) {
                if ($taskOwned.Add([int]$taskProcess.ProcessId)) { $taskAdded = $true }
            }
        }
    } while ($taskAdded)
    foreach ($taskProcess in $taskProcesses) {
        if ($taskProcess.Name -eq 'lean.exe' -and $taskOwned.Contains([int]$taskProcess.ProcessId)) {
            $taskMetric = Get-Process -Id $taskProcess.ProcessId -ErrorAction SilentlyContinue
            if ($taskMetric) {
                $taskPeak = [Math]::Max($taskPeak, $taskMetric.WorkingSet64)
                if ($taskMetric.WorkingSet64 -gt ($MemoryLimitMB * 1MB)) {
                    Stop-Process -Id $taskMetric.Id
                    $taskStopped = $true
                }
            }
        }
    }
    Start-Sleep -Milliseconds 500
    $taskRun.Refresh()
}
$taskRun.WaitForExit()
$taskCode = if ($taskStopped) { 99 } else { $taskRun.ExitCode }
$taskSummary = [ordered]@{
    scope = 'fixed Phase-25 integer table proof; no interval claim until accepted and audited'
    exit_code = $taskCode
    elapsed_seconds = ([DateTime]::UtcNow - $taskStart).TotalSeconds
    observed_peak_working_set_bytes = $taskPeak
    memory_threshold_mb = $MemoryLimitMB
    resource_stop = $taskStopped
    threads = 1
    stack_kb = 16384
    stdout = [IO.Path]::GetFileName($taskOut)
    stderr = [IO.Path]::GetFileName($taskErr)
}
$taskSummary | ConvertTo-Json | Set-Content -LiteralPath $taskResult -Encoding utf8
Get-Content -LiteralPath $taskOut
Get-Content -LiteralPath $taskErr
$taskSummary | ConvertTo-Json
exit $taskCode
