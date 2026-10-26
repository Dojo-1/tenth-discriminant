# Read-only research verification; not part of the Lean CI gates.
$ErrorActionPreference = 'Stop'
$taskManifest = Get-Content (Join-Path $PSScriptRoot 'PHASE40_SOURCES.json') -Raw | ConvertFrom-Json
foreach ($taskSource in $taskManifest.sources) {
    $taskDoc = gh api "repos/$($taskManifest.external_repository)/contents/$($taskSource.path)?ref=$($taskManifest.external_commit)" | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0) { throw "Fetch failed: $($taskSource.path)" }
    $taskBytes = [Convert]::FromBase64String($taskDoc.content)
    $taskHasher = [Security.Cryptography.SHA256]::Create()
    try { $taskHash = ([BitConverter]::ToString($taskHasher.ComputeHash($taskBytes))).Replace('-', '').ToLowerInvariant() }
    finally { $taskHasher.Dispose() }
    if ($taskDoc.sha -ne $taskSource.blob -or $taskBytes.Length -ne $taskSource.bytes -or $taskHash -ne $taskSource.sha256) {
        throw "Frozen-source mismatch: $($taskSource.path)"
    }
    if ($taskSource.path -like '*/proof.tex') {
        $taskOld = gh api "repos/$($taskManifest.external_repository)/contents/$($taskSource.path)?ref=$($taskManifest.historical_recency_control.commit)" | ConvertFrom-Json
        if ($LASTEXITCODE -ne 0 -or $taskOld.sha -ne $taskSource.blob) { throw "Recency-control mismatch: $($taskSource.path)" }
    }
    Write-Output "PASS frozen bytes/blob/hash: $($taskSource.path)"
}
$taskRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$taskDocs = @('README.md', 'STATUS.md', 'TAO_OBJECTIVES_CURRENT.md', 'lean/FORMALIZATION.md',
    'research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md')
$taskCount = 0
foreach ($taskDocPath in $taskDocs) {
    $taskFullPath = Join-Path $taskRoot $taskDocPath
    $taskText = Get-Content $taskFullPath -Raw
    foreach ($taskMatch in [regex]::Matches($taskText, '\[[^\]]*\]\(([^)]+)\)')) {
        $taskTarget = $taskMatch.Groups[1].Value
        if ($taskTarget -match '^(https?://|#|mailto:)') { continue }
        $taskTarget = ($taskTarget -split '#')[0]
        if (-not (Test-Path -LiteralPath (Join-Path (Split-Path $taskFullPath) $taskTarget))) {
            throw "Missing reader target in ${taskDocPath}: $taskTarget"
        }
        $taskCount++
    }
}
Write-Output "PASS $taskCount local reader-link targets in $($taskDocs.Count) selected documents"
Write-Output 'This verifies correspondence and links, not the external mathematical claims.'
