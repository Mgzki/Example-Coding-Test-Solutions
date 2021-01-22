nums = [3,2,3]
target = 6
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(nums, target: int):
        seen = {}
        for i,v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining],i]
            seen[v] = i
        return []
