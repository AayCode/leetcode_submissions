# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head):
        previous = None
        while head:
            front = head.next
            head.next = previous
            previous = head
            head = front
        return previous

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p1 = self.reverseLinkedList(slow)
        p2 = head

        max_twin = float('-inf')

        while p1:
            total = p1.val + p2.val
            if total > max_twin:
                max_twin = total
            p1 = p1.next
            p2 = p2.next

        return max_twin 
