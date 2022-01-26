'''
 Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
''' 

class Solution(object):
    # Time: O(n)
    # Space: O(1)
    def checkPalindrome(self, s, left, right):

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return self.checkPalindrome(s, left+1, right) or self.checkPalindrome(s, left, right-1)

            left += 1
            right -= 1

        return True 
