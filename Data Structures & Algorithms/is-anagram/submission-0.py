class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = [0] * 26
        lst2 = [0] * 26
        for i in s:
            lst1[ord(i) - ord('a')]+=1
        for j in t:
            lst2[ord(j) - ord('a')] +=1
        print(lst1)
        print(lst2)
        return lst1 == lst2