# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        cur = head
        while cur:
            if cur.val not in l1:
                l1.append(cur.val)
            cur = cur.next
        
        sll=ListNode()
        temp = sll
        for i in l1:
            node = ListNode(i)
            temp.next=node
            temp = temp.next
        return sll.next
        

        