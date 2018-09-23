'''

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

'''


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        #标识当前节点和下一层节点
        cur = [root]
        next = []

        #记录最终结果和每一层的结果
        result = [[root.val]]
        result_tmp = []
        #循环，当某层有值的时候
        while len(cur) > 0 :
            #遍历当前层的节点
            for i in range(len(cur)):
                if cur[i].left != None :
                    next.append(cur[i].left)
                    result_tmp.append(cur[i].left.val)
                if cur[i].right != None:
                    next.append(cur[i].right)
                    result_tmp.append(cur[i].right.val)
            cur = next
            next = []

            if len(result_tmp) > 0:
                result.insert(0,result_tmp)
            result_tmp = []

        return result


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e

print(Solution().levelOrderBottom(a))