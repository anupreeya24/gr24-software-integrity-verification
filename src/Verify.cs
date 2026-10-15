using System;
using System.IO;
using System.Security.Cryptography;
using System.Text.RegularExpressions;

class Verify {
    static int Main(string[] args) {
        if (args.Length != 2) {
            Console.WriteLine("Usage: verify.exe <file> <trusted_sha256>");
            return 2;
        }
        string expected = args[1].Trim().ToLowerInvariant();
        if (!Regex.IsMatch(expected, "\\A[0-9a-f]{64}\\z")) {
            Console.WriteLine("ERROR: invalid SHA-256 digest");
            return 2;
        }
        try {
            string actual;
            using (var stream = File.OpenRead(args[0]))
            using (var hash = SHA256.Create()) {
                actual = BitConverter.ToString(hash.ComputeHash(stream)).Replace("-", "").ToLowerInvariant();
            }
            Console.WriteLine("Expected: " + expected);
            Console.WriteLine("Actual:   " + actual);
            bool passed = actual == expected;
            Console.WriteLine(passed ? "PASS: integrity verified" : "FAIL: integrity verification failed");
            return passed ? 0 : 1;
        } catch (IOException error) {
            Console.WriteLine("ERROR: " + error.Message); return 2;
        } catch (UnauthorizedAccessException error) {
            Console.WriteLine("ERROR: " + error.Message); return 2;
        }
    }
}
