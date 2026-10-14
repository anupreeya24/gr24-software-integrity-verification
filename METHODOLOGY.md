# Methodology for software integrity verification

## Purpose
This project demonstrates the SHA-256 integrity check described in the Group 24 report, Prevention of Supply Chain Cyber Attacks Using Software Integrity Verification. The Python program and Windows executable implement the same checksum comparison. The executable is compiled from the supplied C# source.

## Implemented procedure
1. Select an original software artifact and obtain its SHA-256 digest through a trusted channel.
2. Read the candidate artifact incrementally and calculate its SHA-256 digest.
3. Validate that the supplied reference contains exactly 64 hexadecimal characters.
4. Compare the calculated and expected digests.
5. Print the decision and return exit code 0 for a match, 1 for a mismatch, or 2 for invalid input or a file access error.
6. Use that exit code as a release gate. Proceed only when the code is 0.

## Evaluation
Run tests/run_tests.py to execute both implementations against an unchanged artifact, a modified artifact, an invalid digest, a missing file, uppercase digest input and a large artifact. The runner saves observed exit codes to test-results.txt. These are checksum tests; they do not evaluate signatures, provenance or vulnerabilities.

## Proposed extension
The report's complete architecture additionally requires authenticated release metadata, signatures, an authorized signer policy, an SBOM tied to the artifact, authenticated build provenance and a dependency risk policy. These controls are proposed extensions and are not implemented in this checksum demonstration. A full deployment gate must reject the artifact when any mandatory control fails and record the reason.

## Interpretation and limitations
A match means that the candidate matches the supplied reference digest. It does not authenticate the reference, identify a signer or establish that software is safe. If an attacker replaces both the artifact and the expected digest, this demonstration can accept the replacement. Secure builds, independent trust configuration and protected signing credentials are required for the broader workflow.
