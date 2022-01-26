'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
'''


'''
Input: n = 5, bad = 4
[1,2,3,4,5]
       l r 
       m
 isBad(3) = false
 isBad(4) = true
 checkhash(3) = false

'''


def mid_calc(left, right):
    return int(left+(right-left)/2)


class Solution(object):
    #time: O(logn)
    #space: O(1)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if isBadVersion(1):
            return 1
        left = 1
        right = n

        while left <= right:
            mid = int(left+(right-left)/2)
            isBad = isBadVersion(mid)
            prevBad = isBadVersion(mid-1)

            if not isBad:
                left = mid + 1

            elif isBad and prevBad:
                right = mid - 1

            elif isBad and not prevBad:
                return mid
