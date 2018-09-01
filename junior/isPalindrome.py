'''
这道题做的还是挺爽的， 感觉稍微学到了一点思路。 双指针。
'''

class Solution:
    def isPalindrome(self, x):
      x_list = list(map(str, str(x)))
      start = 0
      end = len(x_list) - 1

      while start < end:
          if(x_list[start] == x_list[end]):
              start = start + 1
              end = end -1
          else:
              return False

      return True


a = 1213
print(Solution().isPalindrome(a))
