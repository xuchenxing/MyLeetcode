'''
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。

示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]

提示：
0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
'''

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        #异常处理
        if (len(A) == 0 and len(B) > 0):
            return B.split( )
        if (len(B) == 0 and len(A) > 0):
            return A.split( )
        if (len(A) == 0 and len(B) == 0):
            return []

        #数组准备
        A = A.split( )
        B = B.split( )
        for i in range(len(B)):
            A.append(B[i])
        #存储已发现的相同单词
        same = []
        #存储结果
        result = []
        #双指针找到相同单词
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] == A[j]:
                    same.append(A[i])
                    break

        #不在相同单词中的单词放到结果中
        for i in range(len(A)):
            if A[i] not in same:
                result.append(A[i])

        return result

a = 'apple apple'
b = 'banana'
print(Solution().uncommonFromSentences(a,b))

