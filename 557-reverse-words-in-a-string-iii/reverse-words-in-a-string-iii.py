class Solution:
    def reverse(self, arr, left, right):
        while left < right:
            arr[right], arr[left] = arr[left], arr[right]
            right -= 1
            left += 1

    def reverseWords(self, s: str) -> str:
        s = list(s)

        left = 0
        right = 0
        while right <= len(s):
            if right == len(s) or s[right] == ' ':
                self.reverse(s, left, right - 1)
                left = right + 1
            right += 1

        return "".join(s)
        