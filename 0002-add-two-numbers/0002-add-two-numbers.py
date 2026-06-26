# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while (l1 is not None) or (l2 is not None) or (carry > 0):
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum = val1 + val2 + carry   # adding the linked list values and the carry

            carry = sum // 10   # calcutes the carry
            digit = sum % 10    # stores the unit place value

            current.next = ListNode(digit)
            current = current.next

            # update the linked list to the next pointer
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        return dummy_head.next
            


