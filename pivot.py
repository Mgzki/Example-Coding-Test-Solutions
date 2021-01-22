#
# Determines 'pivot' of an inputed list of values (if it exists)
# Sum of values left of the pivot is equal to sum of values right of the pivot
#

#sample inputs
list = [1,4,6,3,2]
list2 = [5,1,2,2,1]
list3 = [1,1]
nums = [-1,-1,-1,0,1,1]
# method 1
def pivot(nums):
    sums = []
    if len(nums) >= 3:
        for i in range(len(nums)):
            sums.insert(i,sum(nums[:i]) + nums[i])
        for j in range(len(nums)-1):
            if (sums[j] == (sums[-1] - sums[j-1])):
                return j
            continue
    return -1
# method 2
def pivot2(nums):
    sums = sum(nums)
    lsum = 0
    for i,x in enumerate(nums):
        if lsum == (sums - lsum - x):
            return i
        lsum += x
    return -1

