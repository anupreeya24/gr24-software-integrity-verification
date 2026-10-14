# Group 24 Software Integrity Verification

A runnable SHA-256 demonstration accompanying the report Prevention of Supply Chain Cyber Attacks Using Software Integrity Verification.

## GitHub repository
[GitHub repository](https://github.com/anupreeya24/gr24-software-integrity-verification)

## Files
- src/verify.py: Python implementation using only the standard library.
- src/Verify.cs: source for the Windows executable.
- bin/verify.exe: compiled Windows console application.
- build.ps1: executable build script.
- samples/: original and modified demonstration artifacts.
- tests/run_tests.py: tests for Python and the executable.
- test-results.txt: observed test results.
- METHODOLOGY.md: implemented methodology and proposed extensions.

## Requirements
Use Python 3 for the source program and test runner. The executable requires Windows with .NET Framework 4.x; Python is not required for the executable. Extract the ZIP before running commands. Open PowerShell in the extracted project folder.

## Execute the Windows application
```powershell
$digest = (Get-FileHash .\samples\original.txt -Algorithm SHA256).Hash
.\bin\verify.exe .\samples\original.txt $digest
.\bin\verify.exe .\samples\tampered.txt $digest
```
The first invocation should print PASS and return 0. The second should print FAIL and return 1. Inspect `$LASTEXITCODE` immediately after an invocation. Run this console application from a terminal rather than double clicking it.

## Execute the Python source
```powershell
$digest = (Get-FileHash .\samples\original.txt -Algorithm SHA256).Hash
python .\src\verify.py .\samples\original.txt $digest
python .\src\verify.py .\samples\tampered.txt $digest
```
On Linux or macOS, use python3 instead of python and supply the authenticated 64 character SHA-256 digest as the second argument.

## Test and rebuild
```powershell
python .\tests\run_tests.py
powershell -ExecutionPolicy Bypass -File .\build.ps1
```
The rebuild uses the Windows .NET Framework C# compiler. No Python packages are needed.

## Trust and scope
Calculating a digest locally is useful for this controlled demonstration. For a real downloaded release, obtain the expected digest from authenticated release metadata. This project does not implement signature validation, SBOM generation, provenance validation or vulnerability scanning. See METHODOLOGY.md for the full proposed architecture.
