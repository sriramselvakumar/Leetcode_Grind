# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
We are either going to encounter a node that is 
    - at the end of the linkedlist
        For a preceding node: 
            in this case curr.next.next = None  
            just set curr.next = None 
    - in the middle of the linkedlist 
        For a preceding node: 
            in this case curr.next.next != None 
            just set curr.next = curr.next.next 
    - beginning of the linkedlist 
        return None  
'''
# Time: O(n)
# Space: O(1)


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        for i in range(n):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
