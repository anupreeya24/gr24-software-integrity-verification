$ErrorActionPreference = 'Stop'
$compiler = Join-Path $env:WINDIR 'Microsoft.NET\Framework64\v4.0.30319\csc.exe'
New-Item -ItemType Directory -Force (Join-Path $PSScriptRoot 'bin') | Out-Null
& $compiler /nologo /target:exe /optimize+ /out:"$PSScriptRoot\bin\verify.exe" "$PSScriptRoot\src\Verify.cs"
if ($LASTEXITCODE -ne 0) { throw 'Compilation failed' }
