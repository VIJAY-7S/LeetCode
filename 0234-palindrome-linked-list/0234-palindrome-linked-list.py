# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst1=[]
        cur = head
        while cur:
            lst1.append(cur.val)
            cur = cur.next
        
        return lst1==lst1[::-1]
        