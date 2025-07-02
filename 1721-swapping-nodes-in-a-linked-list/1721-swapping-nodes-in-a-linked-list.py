# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst1=[]
        cur = head
        while cur:
            lst1.append(cur.val)
            cur = cur.next
        
        c=lst1[k-1]
        lst1[k-1]=lst1[-k]
        lst1[-k]=c

        sll=ListNode()
        temp=sll
        for i in lst1:
            temp.next=ListNode(i)
            temp=temp.next
        return sll.next
        