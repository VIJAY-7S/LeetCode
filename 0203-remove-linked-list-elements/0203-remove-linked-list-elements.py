# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        lst1=[]
        cur = head
        while cur:
            if cur.val!=val:
                lst1.append(cur.val)
            cur = cur.next
        sll = ListNode()
        temp = sll
        for i in lst1:
            temp.next=ListNode(i)
            temp=temp.next
        return sll.next