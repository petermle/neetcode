from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int, next: ListNode = None):
        self.val = x
        self.next = next

    def set_next(self, next: ListNode):
        self.next = next
        return next

def hasCycle(head: Optional[ListNode]) -> bool:
        # use floyd's cycle detection algorithm
        slow = fast = head
        while fast and fast.next:  # check for null before any assignment
            slow = slow.next
            fast = fast.next.next  # valid bc null at worst

            # fast catches up to slow (there's a cycle)
            if fast == slow:
                return True
        
        # fast reaching end of list means terminating list
        return False

if __name__ == "__main__":
    node_1 = ListNode(3)
    node_2 = ListNode(2)
    node_3 = ListNode(0)
    node_4 = ListNode(-4)

    node_1.set_next(node_2).set_next(node_3).set_next(node_4).set_next(node_2)
    output = hasCycle(node_1)
    expected = True

    if output == expected:
         print("Test case passed.")
