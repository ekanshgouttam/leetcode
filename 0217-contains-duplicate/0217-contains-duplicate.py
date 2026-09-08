class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        max_count = 0
        for i in range(n-1):
            count = 0
            if nums[i] == nums[i+1]:
                count += 1
            max_count = max(max_count, count)
        if max_count >0:
            return True
        else:
            return False

