'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you 
climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''


'''

1 step 
1 

2 steps 
1 + 1 
2

3 steps 
1 + 1 + 1 
1 + 2 
2 + 1 

4 steps 
2 + 2 
1 + 2 + 1 
1 + 1 + 1 + 1 
2 + 1 + 1 
1 + 1 + 2 

5 steps 
2 + 2 + 1 
1 + 2 + 2 
2 + 1 + 2
1 + 1 + 1 + 1 + 1 




[1,2,3,5]
'''


class Solution(object):
    #time: o(n)
    #space: o(n)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 2]

        if n < 3:
            return result[n-1]

        for i in range(3, n+1):
            combinations = result[i-2] + result[i-3]
            result.append(combinations)

        return result[-1]
