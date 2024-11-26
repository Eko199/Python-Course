#Solution 1
from collections import Counter

class Solution:
    def majorityElement(self, nums):
        return sorted(Counter(nums).items(), key = lambda i: -i[1])[0][0]
    
#Solution 2
class Solution2:
    def majorityElement(self, nums):
        counter = Counter(nums)
        size = len(nums)
        return next(i[0] for i in counter.items() if i[1] > size / 2)