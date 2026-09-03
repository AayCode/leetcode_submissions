# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculating length of the linked list
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next

        # Calculating position of the nth node from end, from start.
        d = length - n + 1
        
        # Creating and connecting an extra temp node so that we can have a prev of head also
        temp = ListNode(0)
        temp.next = head

        prev = temp

        i = 0
        while i < d-1:
            prev = prev.next
            i += 1
        
        prev.next = prev.next.next

        return temp.next