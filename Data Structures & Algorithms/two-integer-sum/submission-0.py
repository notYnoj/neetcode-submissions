class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in dct:
                return [dct[t], i]
            else:
                dct[nums[i]] = i
         