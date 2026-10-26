$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
$taskPrevious = @(Get-ChildItem -LiteralPath $PSScriptRoot -Filter 'PHASE39_BUILD_*.result.json' | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw | ConvertFrom-Json })
if (@($taskPrevious | Where-Object { $_.stop_reason }).Count) { throw 'No retry after a Phase39 resource stop' }
if ($taskPrevious.Count -ge 4) { throw 'Phase39 repair-count limit reached' }
$taskSpent = ($taskPrevious | Measure-Object -Property elapsed_seconds -Sum).Sum
if ($null -eq $taskSpent) { $taskSpent = 0 }
$taskLimit = [Math]::Min(600,[Math]::Floor(900-$taskSpent))
if ($taskLimit -le 0) { throw 'Phase39 cumulative proof-build allowance exhausted' }
$taskStamp = [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
$taskPrefix = Join-Path $PSScriptRoot "PHASE39_BUILD_$taskStamp"
$taskTarget = 'TenthDiscriminant.OptimizedAnalyticCutoff'
$taskRun = Start-Process -FilePath (Get-Command lake.exe).Source -WorkingDirectory (Join-Path $taskRepo 'lean') `
  -WindowStyle Hidden -PassThru -ArgumentList @('build',$taskTarget) `
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
      }
    }
  }
  if (([DateTime]::UtcNow-$taskStart).TotalSeconds -gt $taskLimit) { $taskReason = 'time_limit' }
  if ($taskReason) {
    foreach ($taskProcess in $taskProcesses) {
      if ($taskOwned.Contains([int]$taskProcess.ProcessId)) {
        Stop-Process -Id $taskProcess.ProcessId -ErrorAction SilentlyContinue
      }
    }
  }
  Start-Sleep -Milliseconds 500
  $taskRun.Refresh()
}
$taskRun.WaitForExit()
$taskCode = if ($taskReason) {99} elseif ($null -eq $taskRun.ExitCode) {98} else {$taskRun.ExitCode}
$taskSummary = [ordered]@{
  scope='Phase39 fixed200-billion direct analytic cutoff proof attempt, not finite-classification recycling'
  build_target=$taskTarget; attempt=$taskPrevious.Count+1; exit_code=$taskCode
  elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds
  cumulative_before_seconds=$taskSpent; time_limit_seconds=$taskLimit; cumulative_allowance_seconds=900
  observed_peak_working_set_bytes=$taskPeak; memory_threshold_mb=8192; stop_reason=$taskReason
  stdout=[IO.Path]::GetFileName("$taskPrefix.stdout.log"); stderr=[IO.Path]::GetFileName("$taskPrefix.stderr.log")
}
$taskSummary | ConvertTo-Json | Set-Content -LiteralPath "$taskPrefix.result.json" -Encoding utf8
Get-Content -LiteralPath "$taskPrefix.stdout.log" -Tail 80
Get-Content -LiteralPath "$taskPrefix.stderr.log" -Tail 20
$taskSummary | ConvertTo-Json
exit $taskCode
