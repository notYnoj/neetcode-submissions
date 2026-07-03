class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        made = {}
        for i in range(len(nums)):
            if(nums[i] in made):
                continue #will get same results
            fix = nums[i]
            #fix one
            l = 0
            r = len(nums) - 1
            while l < i and r > i:
                left = nums[l]
                right = nums[r]
                if left + fix + right == 0:
                    if [left, fix, right] not in ret:
                        ret.append([left, fix, right])
                    r-=1
                    l+=1
                elif left + fix + right >= 0:
                    r-=1
                else:
                    l+=1
        return ret