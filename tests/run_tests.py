"""Check actual CLI exit codes for Python and Windows implementations."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
original = root / 'samples/original.txt'
expected = hashlib.sha256(original.read_bytes()).hexdigest()
implementations = [('Python', [sys.executable, str(root / 'src/verify.py')])]
if sys.platform == 'win32':
    implementations.append(('Windows executable', [str(root / 'bin/verify.exe')]))
lines, failures = [], 0
with tempfile.TemporaryDirectory(dir=root) as temporary:
    large = Path(temporary) / 'large.bin'
    large.write_bytes(b'integrity-demo' * 1000000)
    cases = [
        ('unchanged', original, expected, 0),
        ('modified', root / 'samples/tampered.txt', expected, 1),
        ('invalid digest', original, 'xyz', 2),
        ('missing file', Path(temporary) / 'missing.bin', expected, 2),
        ('uppercase digest', original, expected.upper(), 0),
        ('large artifact', large, hashlib.sha256(large.read_bytes()).hexdigest(), 0),
    ]
    for name, command in implementations:
        for label, path, digest, wanted in cases:
            result = subprocess.run(command + [str(path), digest], capture_output=True, text=True)
            passed = result.returncode == wanted
            failures += not passed
            lines.append('{} | {} | expected {} | observed {} | {}'.format(name, label, wanted, result.returncode, 'PASS' if passed else 'FAIL'))
            if not passed:
                lines.append(result.stdout + result.stderr)
lines.append('Total failures: {}'.format(failures))
report = '\n'.join(lines) + '\n'
(root / 'test-results.txt').write_text(report, encoding='utf-8')
print(report)
sys.exit(1 if failures else 0)
