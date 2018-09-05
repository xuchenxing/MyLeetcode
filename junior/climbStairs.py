'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

解题思路：
1. 按照人的思路， 首先看每次都走一步的解法，肯定有且只有一种。
2. 以此类推， 所以问题的思路应该是2步的出现次数， 0-n/2
    出现一次，1
    出现2次，n-1
    出现3次，n-2
    。。。
    出现n/2次，n-(2/n-1) = 2/n+1

    GG
    TODO
'''



class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 :
            return 1
        elif n ==2:
            return 2
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)

    def climbStairs1(self, n):
        fbn1 = 0
        fbn2 = 1
        for i in range(1, n+1):
            tmp = fbn1 + fbn2
            fbn1 = fbn2
            fbn2 = tmp

        return fbn2




print(Solution().climbStairs1(100))