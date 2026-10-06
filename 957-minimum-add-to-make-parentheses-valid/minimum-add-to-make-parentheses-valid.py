class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        coun = 0
        count = 0
        for ch in s:
            if ch == "(":
                count += 1
            elif count == 0:
                coun += 1
            else:
                count -= 1

        return abs(count) + abs(coun)

        