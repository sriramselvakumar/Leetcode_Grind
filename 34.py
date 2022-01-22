# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# Explanation
# Set pointer start which points to index 0 
# Set pointer end which points to len(array) - 1 
# Set while loop with condition:  start<=end 
# In While Loop:
#   If array[start] < target then start+=1 
#   Else If array[start] > target then return [-1,-1]
#   If array[end] > target then end-=1 
#   Else if array[end] < target then return [-1,-1]
#   If array[start] == target and array[end] == target return [start,end]


class Solution(object):
    def find_start(self, nums, target):
      if nums[0] == target: 
        return 0 

      left, right = 0, len(nums) - 1 

      while left<=right: 
        mid = int(left + (right - left)/2)

        if nums[mid] == target and nums[mid-1] < target:
          return mid 

        elif nums[mid] < target:
          left = mid + 1 

        else: 
          right = mid -1 
      return -1 

    def find_end(self, nums, target):
      if nums[-1] == target: 
        return len(nums) - 1 

      left, right = 0, len(nums) - 1 

      while left<=right:
        mid = int(left + (right - left)/2)

        if nums[mid] == target and nums[mid+1] > target: 
          return mid 

        elif nums[mid]  > target: 
          right = mid -1 
        else: 
          left = mid + 1 
      return -1 

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0 or nums[-1] < target or nums[0] > target: 
          return [-1,-1]

        start = self.find_start(nums, target)
        end = self.find_end(nums, target)

        return [start, end]
        

        