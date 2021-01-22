class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

# 342
l1 = ListNode()
l1.head = 3
l1.head = 4
l1.head = 2

# 465
l2 = ListNode()
l2.head = 4
l2.head = 6
l2.head = 5

# Given two integers in Linked-List Format, return their sums as a linked list
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        head = ListNode()
        cursor = head
        carry = 0

        while(l1 or l2 or carry):
            cursor.next = ListNode()
            cursor = cursor.next
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry;
            cursor.val = value % 10
            carry = 1 if value >= 10 else 0
            l1 = l1.next if l1 else null
            l2 = l2.next if l2 else null
        return head.next

result = Solution()
