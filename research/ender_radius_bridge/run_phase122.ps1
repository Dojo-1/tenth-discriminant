$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if (@(Get-ChildItem $PSScriptRoot -Filter 'PHASE122_build_*.result.json').Count) { throw 'Phase122 sole invocation already consumed' }
if (Test-Path -LiteralPath (Join-Path $PSScriptRoot 'PHASE122_STARTED.json')) { throw 'Phase122 already started; reconcile the existing handle, never restart' }
$taskFreeze = Get-Content (Join-Path $PSScriptRoot 'PHASE122_FROZEN.json') -Raw | ConvertFrom-Json
foreach ($taskFile in $taskFreeze.files.PSObject.Properties) {
 if ((Get-FileHash -LiteralPath (Join-Path $taskRepo $taskFile.Name) -Algorithm SHA256).Hash.ToLowerInvariant() -ne $taskFile.Value) { throw "Frozen source mismatch: $($taskFile.Name)" }
}
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
$taskPrefix = Join-Path $PSScriptRoot "PHASE122_build_$taskStamp"
$taskExe = Join-Path $env:USERPROFILE '.elan/bin/lake.exe'
$env:PATH = (Split-Path $taskExe) + ';' + $env:PATH
$taskArgs = @('env','lean','-j','1','../research/ender_radius_bridge/Phase122Endpoint.lean')
$taskLimit=300
$Mode='build'
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'Phase122Endpoint.lean') -Destination "$taskPrefix.source.lean"
@{prefix=$taskPrefix;source_sha256=(Get-FileHash -LiteralPath "$taskPrefix.source.lean" -Algorithm SHA256).Hash.ToLowerInvariant()} | ConvertTo-Json | Set-Content (Join-Path $PSScriptRoot 'PHASE122_STARTED.json') -Encoding utf8
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskExe -WorkingDirectory (Join-Path $taskRepo 'lean') -WindowStyle Hidden -PassThru -ArgumentList $taskArgs -RedirectStandardOutput "$taskPrefix.stdout.log" -RedirectStandardError "$taskPrefix.stderr.log"
$taskLive = [ordered]@{pid=$taskRun.Id;started=$taskStart.ToString('o');prefix=$taskPrefix;mode=$Mode;status='running'}
$taskLive | ConvertTo-Json | Set-Content (Join-Path $taskRepo '.agent/PHASE122_LIVE.json') -Encoding utf8
$taskHandle = $taskRun.Handle
$taskOwned = [System.Collections.Generic.HashSet[int]]::new()
[void]$taskOwned.Add($taskRun.Id)
$taskPeak = 0L
$taskReason = ''
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
$taskCode = if ($taskReason) {99} elseif ($null -eq $taskRun.ExitCode) {100} else {$taskRun.ExitCode}
if (-not $taskReason -and (Select-String -LiteralPath @("$taskPrefix.stdout.log","$taskPrefix.stderr.log") -Pattern 'maximum number of heartbeats|maximum recursion depth|deterministic.*timeout' -Quiet)) { $taskReason = 'lean_internal_resource_limit' }
$taskResult = [ordered]@{phase=122;scope='Fixed47.5b actual-field endpoint attempt;standalone only';attempt=1;exit_code=$taskCode;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;time_limit_seconds=$taskLimit;memory_threshold_mb=8192;observed_peak_working_set_bytes=$taskPeak;stop_reason=$taskReason;executable=$taskExe;arguments=$taskArgs;source_snapshot=[IO.Path]::GetFileName("$taskPrefix.source.lean");source_sha256=(Get-FileHash -LiteralPath "$taskPrefix.source.lean" -Algorithm SHA256).Hash.ToLowerInvariant();stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log");stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")}
$taskResult | ConvertTo-Json -Depth 5 | Set-Content "$taskPrefix.result.json" -Encoding utf8
$taskLive.status='terminal'
$taskLive | ConvertTo-Json | Set-Content (Join-Path $taskRepo '.agent/PHASE122_LIVE.json') -Encoding utf8
Get-Content "$taskPrefix.stdout.log" -Tail 15
Get-Content "$taskPrefix.stderr.log" -Tail 10
$taskResult | ConvertTo-Json -Depth 5
exit $taskCode
