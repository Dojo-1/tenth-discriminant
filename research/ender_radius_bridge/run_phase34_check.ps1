param([string]$ProofFile)
$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmss')
$taskPrefix = Join-Path $PSScriptRoot "PHASE34_CHECK_$taskStamp"
$taskRun = Start-Process -FilePath (Get-Command lake.exe).Source `
  -WorkingDirectory (Join-Path $taskRepo 'lean') -WindowStyle Hidden -PassThru `
  -ArgumentList @('env','lean','-j','1','-s','16384',$ProofFile) `
  -RedirectStandardOutput "$taskPrefix.stdout.log" -RedirectStandardError "$taskPrefix.stderr.log"
$taskHandle = $taskRun.Handle
$taskStart = [DateTime]::UtcNow
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
    if ($taskProcess.Name -eq 'lean.exe' -and $taskOwned.Contains([int]$taskProcess.ProcessId)) {
      $taskMetric = Get-Process -Id $taskProcess.ProcessId -ErrorAction SilentlyContinue
      if ($taskMetric) {
        $taskPeak = [Math]::Max($taskPeak,$taskMetric.WorkingSet64)
        if ($taskMetric.WorkingSet64 -gt 8192MB) { $taskReason = 'memory_limit' }
        if (([DateTime]::UtcNow-$taskStart).TotalSeconds -gt 180) { $taskReason = 'time_limit' }
        if ($taskReason) { Stop-Process -Id $taskMetric.Id }
      }
    }
  }
  Start-Sleep -Milliseconds 500
  $taskRun.Refresh()
}
$taskRun.WaitForExit()
$taskCode = if ($taskReason) { 99 } elseif ($null -eq $taskRun.ExitCode) { 98 } else { $taskRun.ExitCode }
$taskSummary = [ordered]@{
  scope='fixed Phase34 pilot only; no global coverage claim'
  proof_file=$ProofFile
  exit_code=$taskCode
  elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds
  observed_peak_working_set_bytes=$taskPeak
  memory_threshold_mb=8192
  time_limit_seconds=180
  stop_reason=$taskReason
  stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log")
  stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")
}
$taskSummary | ConvertTo-Json | Set-Content -LiteralPath "$taskPrefix.result.json" -Encoding utf8
Get-Content -LiteralPath "$taskPrefix.stdout.log"
Get-Content -LiteralPath "$taskPrefix.stderr.log"
$taskSummary | ConvertTo-Json
exit $taskCode
