class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        for i in range(len(nums)):
            if i != 0:
                pref[i] *= pref[i-1] * nums[i]
            else:
                pref[i] = nums[i]
        for i in range(len(nums)-1, -1, -1):
            if i != len(nums) - 1:
                suff[i] *= suff[i+1] * nums[i]
            else:
                suff[i] = nums[i]
        ret = [0] * n
        for i in range(n):
            if i == 0:
                ret[i] = suff[i+1]
            elif i == n-1:
                ret[i] = pref[i-1]
            else:
                ret[i] = pref[i-1] * suff[i+1]
        return ret