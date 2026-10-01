class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        j="".join(sorted(s))
        k="".join(sorted(t))
        if j==k:
            return True
        return False    