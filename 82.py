'''
 Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    #time: O(n)
    #space: O(1)
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0, head)
        left = dummy
        right = head

        prev = None

        while right:

            if right and right.next and right.val != right.next.val:

                if prev is None:
                    left.next = right
                    left = left.next

                elif prev and right.val != prev.val:
                    left.next = right
                    left = left.next

            elif right and right.next is None:
                if right.val != prev.val:
                    left.next = right
                elif right.val == prev.val:
                    left.next = None

            prev = right

            right = right.next

        return dummy.next
