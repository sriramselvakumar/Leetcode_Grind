# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


# Explanation: 
# Iterate through s1: 
#   If that character in s1 is already a key in the dict then increment its frequency value 
#   else If that character in s1 is not a key in dict then add it as a key and set its freq to 1

# Iterate through s2: 
#   If that character isn't a key in dict then return false 
#   else If that character is a key in dict and the count is larger than 0 then decrement the count and keep moving 
#   else if that character is a key in dict and the count is already 0 then return false 

# iterate through all keys of dict. If any of them have a value that's not 0 then return False

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagramDict = dict()
        for i in s: 
            if i in anagramDict:
                anagramDict[i] = anagramDict[i] + 1
            else:
                anagramDict[i] = 1

        for i in t: 
            if i not in anagramDict:
                return False 

            elif(anagramDict[i] > 0 ):
                anagramDict[i] = anagramDict[i] - 1 

            elif(anagramDict[i] == 0):
                return False

        for key in anagramDict:
            if(anagramDict[key] != 0):
                return False

        return True 