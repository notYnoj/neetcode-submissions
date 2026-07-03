class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = [ ([0] * 26) for _ in range(len(strs))]
        print(ls)
        for i in range(len(strs)):
            for j in strs[i]:
                ls[i][ord(j) - ord("a")]+=1
        dct = {}
        for i in range(len(strs)):
            tp = tuple(ls[i])
            if tp not in dct:
                dct[tp] = [strs[i]]
            else:
                dct[tp].append(strs[i])
        ret = []
        for val in dct.values():
            ret.append(val)
        return ret