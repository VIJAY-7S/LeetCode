# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst=[]
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        lst.pop(-n)
        sll=ListNode()
        temp = sll
        for i in lst:
            node = ListNode(i)
            temp.next = node
            temp = temp.next
        return sll.next

        