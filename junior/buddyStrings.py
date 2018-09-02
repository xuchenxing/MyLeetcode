class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        #标识有多少个字符不一样
        count = 0
        #标识不一样的两个字符的位置
        pos = []

        if len(A) != len(B):
            return False

        A_list = list(map(str, A))
        B_list = list(map(str, B))

        #循环标志位
        i = 0
        while i < len(A) and count<=2:
            if (A_list[i] != B_list[i]):
                count = count + 1
                pos.append(i)
            i = i + 1
        #如果只有一个位置不同， 直接返回falase
        if(count == 1) :
            return False
        #如果字符全部一样， 判断字符串中有没有两个以上相同的字符
        if(count == 0) :
            seen = set()
            for a in A_list:
                if a in seen:
                    return True
                seen.add(a)
            return False
        #如果有两个字符不一样， 判断是否对应相同
        if(count == 2 and A_list[pos[0]] == B_list[pos[1]] and A_list[pos[1]] == B_list[pos[0]]):
            return True

        return False


a = 'aa'
b = 'aa'
print(Solution().buddyStrings(a,b))




