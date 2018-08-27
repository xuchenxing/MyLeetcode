def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    #游标
    cur = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[cur] = nums[i]
            cur = cur + 1


    return nums,cur



print(removeElement([3,2,2,3],3))