class Solution:
    def sumOfSquaresOfDigit(self, n):
        sum = 0
        while n != 0:
            digit = n % 10
            sum += digit ** 2
            n = n//10

        return sum

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while fast != 1:
            slow = self.sumOfSquaresOfDigit(slow)
            fast = self.sumOfSquaresOfDigit(self.sumOfSquaresOfDigit(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False
        
        return True

        