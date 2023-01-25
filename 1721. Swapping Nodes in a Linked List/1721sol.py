# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next

        cur_tgt = head

        for i in range(k-1):
            cur_tgt = cur_tgt.next

        cur_tgt2 = head
        for i in range(count - k):
            cur_tgt2 = cur_tgt2.next

        tmp = cur_tgt.val
        cur_tgt.val = cur_tgt2.val
        cur_tgt2.val = tmp

        return head