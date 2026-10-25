$ErrorActionPreference = 'Stop'
$taskSeeds = @(3,27,35,59,75,123,131,139,147,163,179)
$taskStart = [DateTime]::UtcNow
$taskResults = [System.Collections.Generic.List[object]]::new()
$taskFailed = $false
for ($taskIndex=0; $taskIndex -lt $taskSeeds.Count; $taskIndex++) {
  $taskRemaining = [Math]::Floor(720-([DateTime]::UtcNow-$taskStart).TotalSeconds)
  $taskSkip = if ($taskRemaining -le 0) { 'aggregate_time_limit' } elseif ($taskFailed) { 'prior_seed_failed' } else { '' }
  if ($taskSkip) {
    $taskResults.Add([ordered]@{seed_index=$taskIndex;seed=$taskSeeds[$taskIndex];status='skipped';reason=$taskSkip})
    continue
  }
  $taskLimit = [Math]::Min(180,$taskRemaining)
  $taskBlockStart = [DateTime]::UtcNow
  $taskProof = "../research/ender_radius_bridge/Phase36Seed${taskIndex}Check.lean"
  powershell -NoProfile -File (Join-Path $PSScriptRoot 'run_phase36_check.ps1') `
    -ProofFile $taskProof -TimeLimitSeconds $taskLimit
  $taskCode = $LASTEXITCODE
  $taskRecord = Get-ChildItem -LiteralPath $PSScriptRoot -Filter 'PHASE36_CHECK_*.result.json' | Where-Object { $_.LastWriteTimeUtc -ge $taskBlockStart } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if ($null -eq $taskRecord) { $taskCode = 98 } else {
    $taskRaw = Get-Content -LiteralPath $taskRecord.FullName -Raw | ConvertFrom-Json
    if ($taskRaw.proof_file -ne $taskProof -or $taskRaw.exit_code -ne $taskCode) { $taskCode=98 }
  }
  $taskResults.Add([ordered]@{seed_index=$taskIndex;seed=$taskSeeds[$taskIndex];status='terminal';exit_code=$taskCode;record=$taskRecord.Name})
  if ($taskCode -ne 0) { $taskFailed=$true }
}
$taskSummary = [ordered]@{scope='Phase36 candidate ALL785 full-interval fiber pilot; classification requires complete masks/semantics/coverage';aggregate_time_limit_seconds=720;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;seeds=$taskResults}
$taskSummary | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'PHASE36_PILOT_RESULTS.json') -Encoding utf8
$taskSummary | ConvertTo-Json -Depth 8
