# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst1=[]
        cur = head
        while cur:
            lst1.append(cur.val)
            cur = cur.next
        
        l=len(lst1)
        j=0
        for i in range(l//k):
            lst1[j:j+k] = lst1[j:j+k][::-1]
            j+=k
        sll=ListNode()
        temp=sll
        for i in lst1:
            temp.next=ListNode(i)
            temp=temp.next
        return sll.next
        
        