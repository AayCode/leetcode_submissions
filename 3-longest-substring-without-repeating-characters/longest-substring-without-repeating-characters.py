class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ptr = 0
        maxx = 0

        # p w w k e w
        #           i
        #       p
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[ptr])
                ptr += 1

            seen.add(s[i])
            maxx = max(maxx, len(seen))

        return maxx

        

        