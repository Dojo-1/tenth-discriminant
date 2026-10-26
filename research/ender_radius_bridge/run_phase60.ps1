$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if (@(Get-ChildItem $PSScriptRoot -Filter 'PHASE60_run_*.result.json').Count -ge 1) { throw 'One registered invocation already used' }
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
$taskPrefix = Join-Path $PSScriptRoot "PHASE60_run_$taskStamp"
$taskSource = Join-Path $PSScriptRoot 'Phase60BoundaryCheck.py'
Copy-Item -LiteralPath $taskSource -Destination "$taskPrefix.source.py"
$taskHash = (Get-FileHash -Algorithm SHA256 -LiteralPath "$taskPrefix.source.py").Hash.ToLowerInvariant()
$taskExe = (Get-Command python.exe).Source
$taskStart = [DateTime]::UtcNow
$taskRun = Start-Process -FilePath $taskExe -WorkingDirectory $taskRepo -WindowStyle Hidden -PassThru -ArgumentList @('-u',$taskSource) -RedirectStandardOutput "$taskPrefix.stdout.json" -RedirectStandardError "$taskPrefix.stderr.log"
$taskHandle = $taskRun.Handle
$taskPeak = 0L
$taskReason = ''
while (-not $taskRun.HasExited) {
    $taskMetric = Get-Process -Id $taskRun.Id -ErrorAction SilentlyContinue
    if ($taskMetric) { $taskPeak = [Math]::Max($taskPeak,$taskMetric.WorkingSet64); if ($taskMetric.WorkingSet64 -gt 256MB) { $taskReason='memory_limit' } }
    if (([DateTime]::UtcNow-$taskStart).TotalSeconds -gt 60) { $taskReason='time_limit' }
    if ($taskReason) { Stop-Process -Id $taskRun.Id -ErrorAction SilentlyContinue }
    Start-Sleep -Milliseconds 100
    $taskRun.Refresh()
}
$taskRun.WaitForExit()
$taskCode = if ($taskReason) {99} elseif ($null -eq $taskRun.ExitCode) {98} else {$taskRun.ExitCode}
$taskResult = [ordered]@{phase=60;attempt=1;exit_code=$taskCode;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;time_limit_seconds=60;memory_threshold_mb=256;observed_peak_working_set_bytes=$taskPeak;stop_reason=$taskReason;source_sha256=$taskHash;source_snapshot=[IO.Path]::GetFileName("$taskPrefix.source.py");stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.json");stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log");executable=$taskExe}
$taskResult | ConvertTo-Json -Depth 5 | Set-Content "$taskPrefix.result.json" -Encoding utf8
Get-Content "$taskPrefix.stdout.json"
$taskResult | ConvertTo-Json -Depth 5
exit $taskCode
