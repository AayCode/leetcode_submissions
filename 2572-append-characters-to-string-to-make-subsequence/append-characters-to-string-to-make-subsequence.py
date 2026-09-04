class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0 
        n = len(t)
        for a in s:
            if i < n and t[i] == a:
                i += 1
        return n - i