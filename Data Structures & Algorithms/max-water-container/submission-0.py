class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mxArea = 0
        for length in range(len(heights)):
            for left in range(len(heights)-length):

                mxArea = max(mxArea, min(heights[left], heights[left+length]) * length)
        return mxArea