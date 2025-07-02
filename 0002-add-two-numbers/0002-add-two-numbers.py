# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        num2=[]
        while l1 and l2:
            num1.append(str(l1.val))
            l1=l1.next
        while l2:
            num2.append(str(l2.val))
            l2=l2.next
        n1 = int(''.join(num1)[::-1])
        n2 = int(''.join(num2)[::-1])
        r=str(n1+n2)
        
        lst = [int(x) for x in r[::-1]]
        sll=ListNode()
        temp = sll
        for i in lst:
            temp.next=ListNode(i)
            temp = temp.next
        return sll.next
        