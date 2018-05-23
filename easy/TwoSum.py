#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# I am also under the assumption that we are not given a sorted array
class Solution:
    def twoSum(self, nums, target):
        index = 0
        index2 = 1
        while(index < len(nums)):
            if((nums[index] + nums[index2]) == target):
                return [index, index2]
            if(index2 == len(nums)-1):
                index = index + 1
                index2 = index + 1
            else:
                index2 = index2 + 1
