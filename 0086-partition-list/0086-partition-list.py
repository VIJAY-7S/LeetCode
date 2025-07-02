# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1=[]
        l2=[]
        cur = head
        while cur:
            if cur.val<x:
                l1.append(cur.val)
            else:
                l2.append(cur.val)
            cur = cur.next
        sll=ListNode()
        temp = sll
        for i in (l1+l2):
            node=ListNode(i)
            temp.next=node
            temp=temp.next
        return sll.next
        