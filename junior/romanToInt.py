'''

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

'''


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #构建数据字典
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        i = 0
        while i < len(s):
            #当前字母小于前一个字母时，加上当前字母数字，减去两倍前一个字母的数字
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                result = result + roman[s[i]] - 2 * roman[s[i-1]]
            else:
                result = result + roman[s[i]]
            i = i + 1
        return result




a = 'CMIMMIXIII'
print(Solution().romanToInt(a))


