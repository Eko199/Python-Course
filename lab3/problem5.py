from collections import Counter

class Solution:
    def kWeakestRows(self, mat, k):
        return [i for i, _ in sorted(enumerate(mat), key = lambda ir: (Counter(ir[1])[1], ir[0]))][:k]