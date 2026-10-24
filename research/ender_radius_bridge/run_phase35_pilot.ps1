$ErrorActionPreference = 'Stop'
$taskManifest = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'PHASE35_MANIFEST.json') -Raw | ConvertFrom-Json
$taskStart = [DateTime]::UtcNow
$taskResults = [System.Collections.Generic.List[object]]::new()
$taskFailed = @{}
foreach ($taskBlock in $taskManifest.blocks) {
  $taskRemaining = [Math]::Floor(720-([DateTime]::UtcNow-$taskStart).TotalSeconds)
  $taskSkip = if ($taskRemaining -le 0) { 'aggregate_time_limit' } elseif ($taskFailed.ContainsKey([int]$taskBlock.quotient)) { 'prior_block_failed_for_quotient' } else { '' }
  if ($taskSkip) {
    $taskResults.Add([ordered]@{quotient=$taskBlock.quotient;seed_index=$taskBlock.seed_index;seed=$taskBlock.seed;status='skipped';reason=$taskSkip})
    continue
  }
  $taskLimit = [Math]::Min(180,$taskRemaining)
  $taskBlockStart = [DateTime]::UtcNow
  powershell -NoProfile -File (Join-Path $PSScriptRoot 'run_phase35_check.ps1') `
    -ProofFile "../research/ender_radius_bridge/$($taskBlock.proof_file)" -TimeLimitSeconds $taskLimit
  $taskCode = $LASTEXITCODE
  $taskRecord = Get-ChildItem -LiteralPath $PSScriptRoot -Filter 'PHASE35_CHECK_*.result.json' | Where-Object { $_.LastWriteTimeUtc -ge $taskBlockStart } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if ($null -eq $taskRecord) { $taskCode = 98 }
  $taskResults.Add([ordered]@{quotient=$taskBlock.quotient;seed_index=$taskBlock.seed_index;seed=$taskBlock.seed;status='terminal';exit_code=$taskCode;record=$taskRecord.Name})
  if ($taskCode -ne 0) { $taskFailed[[int]$taskBlock.quotient] = $true }
}
$taskSummary = [ordered]@{scope='fixed Phase35 pilot, not full-range coverage';aggregate_time_limit_seconds=720;elapsed_seconds=([DateTime]::UtcNow-$taskStart).TotalSeconds;blocks=$taskResults}
$taskSummary | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'PHASE35_PILOT_RESULTS.json') -Encoding utf8
$taskSummary | ConvertTo-Json -Depth 8
