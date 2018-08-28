class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) -2


        while i >= 0 and nums[i+1] <= nums[i]:
            i = i - 1

        if i>=0:
            j = len(nums) - 1
            while j>0 and nums[j] <= nums[i]:
                j = j - 1

            self.swap(nums, i, j)

        self.reverse(nums, i+1)


    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums, start):
        cur = len(nums) - 1
        while cur > start:
            self.swap(nums, cur, start)
            cur = cur - 1
            start = start + 1


a = [1,2,3]
Solution().nextPermutation(a)
print(a)