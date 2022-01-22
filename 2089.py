# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100


class Solution(object):

    def find_start(self, nums, target): 
      if nums[0] == target: 
        return 0 

      left, right = 0, len(nums) -1 

      while left <= right: 
        mid = int(left + (right - left)/2)
        if nums[mid] == target and nums[mid-1] < target: 
          return mid 

        elif nums[mid] < target:
          left = mid + 1 

        else 
          right = mid - 1 

      return -1 

    def find_end(self, nums, target): 
      if nums[-1] == target: 
        return len(nums) -1 

      left, right = 0, len(nums) -1 

      while left <= right: 
        mid = int(left + (right - left)/2)
        if nums[mid] == target and nums[mid + 1] > target: 
          return mid 

        elif nums[mid] > target: 
          right = mid -1 
        else: 
          left = mid + 1 

      return -1 

    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()
        start = self.find_start(nums, target)
        end = self.find_end(nums, target)

        if start == -1 or end == -1: 
          return -1 

        return list(range(start, end+1))

         
