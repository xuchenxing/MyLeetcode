'''


给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head

        while head != None and current.next != None:
            if current.next.val == current.val:
                current.next = current.next.next
            else :
                current = current.next

        return head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(2)

a.next = b
b.next = c
c.next = d

re = Solution().deleteDuplicates(a)
while re.next != None:
    print(re.val)
    re = re.next
print(re.val)


