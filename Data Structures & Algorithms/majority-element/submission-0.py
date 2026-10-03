from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen=defaultdict(int)
        n=len(nums)
        for num in nums:
            seen[num]+=1
            if seen[num]>n/2:
                return num


        