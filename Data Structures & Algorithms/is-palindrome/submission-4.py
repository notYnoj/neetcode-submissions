class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        s = s.upper()
        while l < r:
            while l<len(s) and not s[l].isalnum():
                l+=1
            while r > -1 and not s[r].isalnum():
                r-=1
            if l>=r:
                return True
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                print(s[:l+1])
                print(s[r:])
                print(l, r)
                return False
        return True