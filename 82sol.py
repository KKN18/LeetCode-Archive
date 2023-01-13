# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(-1)
        start.next = head
        prev = start
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr:
                    if curr.next == None or curr.val != curr.next.val:
                        curr = curr.next
                        break
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return start.next
