class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret += i
            ret+="177787"
        return ret
    def decode(self, s: str) -> List[str]:
        ls = s.split("177787")
        ls.pop()
        return ls