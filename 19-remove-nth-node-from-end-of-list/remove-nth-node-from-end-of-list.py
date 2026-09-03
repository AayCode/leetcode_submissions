# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head

        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        
        d = length - n + 1

        prev = temp
        curr = head

        i = 0
        while i < d-1:
            prev = prev.next
            curr = curr.next
            i += 1
        
        prev.next = curr.next

        return temp.next