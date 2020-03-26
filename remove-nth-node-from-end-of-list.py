# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
            
        if length == 1 and n ==1:
            return None
        
        steps = length - n -1
        node = head
        print (length, steps)
        
        if steps > -1:
            while steps > 0:
                node = node.next
                steps -= 1
            node.next = node.next.next
        else:
            head = head.next

        return head