# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if p1 and p2 are None
        #   return None
        # If p1 is None
        #   sum = output.val + p2.val
        # elif p2 is None
        #   sum = output.val + p1.val
        # else
        #   sum = p1.val + p2.val
        # ones = sum % 10
        # carry = 0 + int (sum / 10)
        # output.val = output.val + ones
        # output.next = recursion(ListNode(carry, next=None), p1.next, p2.next)
        # return output
        return self.recursion(ListNode(0, None), l1, l2)
    
    def recursion(self, output: Optional[ListNode], p1: Optional[ListNode], p2: Optional[ListNode]):
        if p1 is None and p2 is None:
            if output.val == 1:
                return output
            else:
                return None
        if p1 is None:
            sum = output.val + p2.val
        elif p2 is None:
            sum = output.val + p1.val
        else:
            sum = output.val + p1.val + p2.val
        ones = sum % 10
        carry = int (sum / 10)
        output.val = ones
        output.next = self.recursion(ListNode(carry, None), None if p1 is None else p1.next, None if p2 is None else p2.next)
        return output
        
            
    
        
        