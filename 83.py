'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


class Solution(object):
    #time: O(n)
    #Memory: O(1)
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        if head.next is None:
            return head

        left = head
        right = head

        while True:
            if right is None:
                left.next = None
                break
            elif right.val != left.val:
                left.next = right
                left = left.next

            right = right.next

        return head
