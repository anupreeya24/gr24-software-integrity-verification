"""Compare an artifact with a SHA-256 digest obtained from a trusted channel."""
import hashlib
import sys
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        for chunk in iter(lambda: stream.read(8192), b''):
            digest.update(chunk)
    return digest.hexdigest()


def main(args=None):
    args = sys.argv[1:] if args is None else args
    if len(args) != 2:
        print('Usage: python src/verify.py <file> <trusted_sha256>')
        return 2
    path, expected = Path(args[0]), args[1].strip().lower()
    if len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
        print('ERROR: invalid SHA-256 digest')
        return 2
    try:
        actual = sha256_file(path)
    except OSError as error:
        print('ERROR:', error)
        return 2
    print('Expected:', expected)
    print('Actual:  ', actual)
    passed = actual == expected
    print('PASS: integrity verified' if passed else 'FAIL: integrity verification failed')
    return 0 if passed else 1


if __name__ == '__main__':
    sys.exit(main())
