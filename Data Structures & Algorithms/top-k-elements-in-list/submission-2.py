from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1          # counting stays the same

        # sort keys by their count, highest first
        ls = sorted(seen, key=lambda x: seen[x], reverse=True)
        return ls[:k]               # take first k