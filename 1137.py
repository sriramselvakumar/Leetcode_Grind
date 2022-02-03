'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''


class Solution(object):
    #time: O(n)
    #space: O(n)
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = [0, 1, 1]

        if n < 3:
            return result[n]

        for i in range(3, n+1):
            number = result[i-1] + result[i-2] + result[i-3]
            result.append(number)

        return result[-1]
