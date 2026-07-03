class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mxArea = 0
        l = 0
        r = len(heights) - 1
        mxArea = 0
        while l < r:
            mxArea = max(mxArea, (r-l) * min(heights[l], heights[r]))
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1 #doesnt matter if equal will always produce less area
        return mxArea