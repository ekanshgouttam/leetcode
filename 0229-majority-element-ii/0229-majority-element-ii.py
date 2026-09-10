class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
            if hash_map[num] > n//3 and num not in result:
                result.append(num)
        return result