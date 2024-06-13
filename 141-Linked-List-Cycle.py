# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        exists = set()

        current = head

        while current and current.next:
            if current not in exists:
                exists.add(current)
            else:
                return True
            
            current = current.next
        
        return False