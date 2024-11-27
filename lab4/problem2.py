# Preconditions
import os
import math

class LAIKA:
    def __init__(self, path: str, caeser_key: int) -> None:
        self.path = path
        self.caeser_key = caeser_key

    def encode(self, string: str, n: int) -> list[str]:
        first: str = ""
        last: str = ""

        for i in range(len(string)):
            if i % 2 == 0:
                first += string[i]
            else:
                last = string[i] + last

        encoded: str = first + last
        result: list[str] = [encoded[i - n:i] for i in range(n, len(encoded) + n, n)]

        return result
    
    def decode(self, encoded: list[str]) -> str:
        string: str = "".join(encoded)
        result: str = ""

        for i in range(math.floor(len(string) / 2)):
            result += string[i] + string[-i - 1]

        if len(string) % 2 == 1:
            result += string[math.floor(len(string) / 2)]

        return result
    
    def encode_to_files(self, string: str, n: int) -> str:
        encoded: list[str] = self.encode(string, n)

        fileNames: list[str] = ["".join(chr(ord("a") + (ord(c) - ord("a") + self.caeser_key) % 26) for c in part) for part in encoded] + [""]

        for i, content in enumerate(encoded):
            path: str = os.path.join(self.path, fileNames[i])
            
            if os.path.exists(path):
                raise FileExistsError(path)

            with open(path, "w") as file:
                file.writelines([fileNames[i + 1] + "\n", content])

        return fileNames[0]
    
    def decode_from_files(self, fileName: str) -> str:
        encoded: list[str] = []

        while fileName != "":
            path: str = os.path.join(self.path, fileName)
            
            if not os.path.exists(path):
                raise FileNotFoundError(path)

            with open(path) as file:
                fileName = file.readline().strip()
                encoded.append(file.readline().strip())

        return self.decode(encoded)

# Tests

root_dir = "task_2"

if not os.path.exists(root_dir):
    os.makedirs(root_dir)

l = LAIKA(root_dir, 3)

# encode
assert l.encode("abcdefg", 2) == ["ac", "eg", "fd", "b"]
assert l.encode("abcdefg", 3) == ["ace", "gfd", "b"]
assert l.encode("abcdefg", 5) == ["acegf", "db"]
assert l.encode("abcdefghijkl", 1) == ["a", "c", "e", "g", "i", "k", "l", "j", "h", "f", "d", "b"]
assert l.encode("abcdefghijkl", 2) == ["ac", "eg", "ik", "lj", "hf", "db"]
assert l.encode("abcdefghijkl", 3) == ["ace", "gik", "ljh", "fdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 12) == ["acegikljhfdb"]
assert l.encode("abcdefghijkl", 24) == ["acegikljhfdb"]


# decode
assert l.decode(["ac", "eg", "fd", "b"]) == "abcdefg"
assert l.decode(l.encode("abcdefg", 3)) == "abcdefg"
assert l.decode(l.encode("abcdefg", 5)) == "abcdefg"
assert l.decode(l.encode("abcdefghijkl", 1)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 2)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 3)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 12)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 24)) == "abcdefghijkl"


# encode_to_files
l1 = LAIKA(root_dir, 4)
assert l1.encode_to_files("abcdefghijkl", 3) == "egi"

assert sorted(os.listdir(root_dir)) == ["egi", "jhf", "kmo", "pnl"]

with open(os.path.join(root_dir, "egi")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "kmo"
assert content == "ace"

with open(os.path.join(root_dir, "jhf")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == ""
assert content == "fdb"

with open(os.path.join(root_dir, "kmo")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "pnl"
assert content == "gik"

with open(os.path.join(root_dir, "pnl")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "jhf"
assert content == "ljh"


# decode_from_files
assert l1.decode_from_files("egi") == "abcdefghijkl"

# Exception

try:
    l1.encode_to_files("abcdefghijkl", 3)
except FileExistsError:
    assert True
except Exception:
    assert False


try:
    l1.decode_from_files("non-existing-file")
except FileNotFoundError:
    assert True
except Exception:
    assert False

print("✅ All OK! +2 points")