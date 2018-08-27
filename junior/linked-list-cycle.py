# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False

        fast = head
        slow = head

        while fast.next != None:
            fast = fast.next.next

            if fast == None:
                return False

            slow = slow.next

            if fast == slow:
                return True

        return False
