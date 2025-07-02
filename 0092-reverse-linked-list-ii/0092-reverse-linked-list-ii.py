# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d1=[]
        cur = head
        while cur:
            d1.append(cur.val)
            cur = cur.next
        d2=d1[left-1:right]
        d3 = d1[:left-1]+d2[::-1]+d1[right:]

        sll=ListNode()
        temp=sll
        for i in d3:
            temp.next=ListNode(i)
            temp = temp.next
        return sll.next
        