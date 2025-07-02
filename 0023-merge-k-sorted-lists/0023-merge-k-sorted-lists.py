# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l1=[]
        for i in lists:
            cur = i
            while cur:
                l1.append(cur.val)
                cur = cur.next
        
        l1.sort()
        sll=ListNode()
        temp = sll
        for i in l1:
            node = ListNode(i)
            temp.next=node
            temp = temp.next
        
        return sll.next


        