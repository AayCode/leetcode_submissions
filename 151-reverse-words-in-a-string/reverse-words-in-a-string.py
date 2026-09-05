class Solution:
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)

        # Remove extra spaces and compact the string
        slow = 0
        fast = 0

        while fast < n:
            if s[fast] != ' ':
                if slow > 0:
                    s[slow] = ' '
                    slow += 1

                while fast < n and s[fast] != ' ':
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
            else:
                fast += 1

        # Reverse the entire valid portion
        self.reverse(s, 0, slow - 1)

        # Reverse each individual word
        left = 0
        right = 0

        while right <= slow:
            if right == slow or s[right] == ' ':
                self.reverse(s, left, right - 1)
                left = right + 1
            right += 1

        return "".join(s[:slow])
