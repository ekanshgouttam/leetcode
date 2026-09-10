class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num]>n//2:
                return num