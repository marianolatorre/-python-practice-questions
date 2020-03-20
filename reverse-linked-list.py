# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        data = []
        ite = head
        while ite is not None:
            data.append(ite.val)
            ite = ite.next
        prev = ListNode()
        
        
        for x in data:
            prev.val = x
            b = ListNode()
            b.next = prev
            prev = b
        
        prev=prev.next
        
        return prev
