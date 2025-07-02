from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d1=deque()
        cur = head
        while cur:
            d1.append(cur.val)
            cur = cur.next
        
        d1.rotate(k)
        sll=ListNode()
        temp = sll
        for i in d1:
            node = ListNode(i)
            temp.next=node
            temp = temp.next
        return sll.next