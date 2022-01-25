# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Logic

# Traverse through nums
#     If the value is already in dict then increment frequency
#     Else set the value as a key and its value as 1

# Traverse through nums
#     result = target - nums[i]
#     if result = nums[i] and dict[nums[i]] > 1
#         return [nums[i], nums[i]]

#     else if result != nums[i] and dict[nums[i]] > 0
#         return [result, nums[i]]

class Solution(object):
    # Time : O(n)
    # Space : O(n)
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
        arrayDict = dict()

        numbers = []

        result = []

        for num in nums:
            if num in arrayDict:
                arrayDict[num] += 1
            else:
                arrayDict[num] = 1
        for num in nums:
            otherNum = target - num
            if otherNum == num and arrayDict[otherNum] > 1:
                numbers = [num, otherNum]
                break
            elif otherNum != num and otherNum in arrayDict:
                numbers = [num, otherNum]
                break

        for count, value in enumerate(nums):
            if value == numbers[0]:
                result.append(count)
                break

        for count, value in enumerate(nums):
            if value == numbers[1] and count != result[0]:
                result.append(count)
                break

        return result
