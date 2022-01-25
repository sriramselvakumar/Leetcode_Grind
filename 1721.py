'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
'''

'''
N = 2
[D,100,90]
 r   l    

'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    #time : O(n)
    #space: O(1)
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(0, head)

        left = dummy
        for i in range(k-1):
            left = left.next

        right = dummy
        fast = head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            right = right.next
            fast = fast.next

        left_next_ref = left.next.next
        right_next_ref = right.next.next
        left_next = left.next
        right_next = right.next

        if left.next is right:
            right_next.next = left.next
            left.next = right_next

            left_next.next = right_next_ref
            return dummy.next

        if right.next is left:
            left_next.next = left
            right.next = left_next

            left.next = left_next_ref
            return dummy.next

        right_next.next = left_next_ref
        left.next = right_next

        left_next.next = right_next_ref
        right.next = left_next

        return dummy.next
