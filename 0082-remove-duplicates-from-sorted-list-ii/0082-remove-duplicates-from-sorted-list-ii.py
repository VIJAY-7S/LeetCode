# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1={}
        cur = head
        while cur:
            if cur.val not in d1:
                d1[cur.val]=1
            else:
                d1[cur.val]+=1
            cur = cur.next
        
        sll=ListNode()
        temp = sll
        for key in d1:
            if d1[key]==1:
                node = ListNode(key)
                temp.next=node
                temp = temp.next
        return sll.next
                
        