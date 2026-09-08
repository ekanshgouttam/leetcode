class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        hash_set = set()
        for i in range(n):
            for j in range(i+1, n):
                my_set = set()
                for k in range(j+1, n):
                    fourth = target - (nums[i]+nums[j]+nums[k])
                    if fourth in my_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        hash_set.add(tuple(temp))
                    my_set.add(nums[k])
        return [list(ans) for ans in hash_set]