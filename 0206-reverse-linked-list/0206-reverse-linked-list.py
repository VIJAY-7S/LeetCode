# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        sll=ListNode()
        temp=sll
        for i in stack[::-1]:
            node = ListNode(i)
            temp.next=node
            temp=temp.next
        return sll.next