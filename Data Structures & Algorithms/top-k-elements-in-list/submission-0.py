class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i]+=1
        ls = sorted(dct.items(), key = lambda x : x[1])
        ret = []
        for i in range(len(ls)-1, -1, -1):
            ret.append(ls[i][0])
            k-=1
            if(k == 0):
                break
        return ret