
nums = [0,0,1,1,1,2,2,3,3,4]

count = 1
for i in range(1, len(nums)):
    if (nums[i] != nums[i - 1]):

        nums[count] = nums[i]
        count = count + 1
print(count)
for i in range(count, len(nums)):
    nums.remove(nums[count ])
print(nums)