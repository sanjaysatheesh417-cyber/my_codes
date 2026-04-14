#https://leetcode.com/problems/add-two-numbers/

solutions:
#using nested list operations
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        curr1 = l1
        while curr1:
            num1 += str(curr1.val)
            curr1 = curr1.next
        num2 = ""
        curr2 = l2
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next
        total = int(num1[::-1]) + int(num2[::-1])

        dummy = ListNode(0)
        curr = dummy
        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next
