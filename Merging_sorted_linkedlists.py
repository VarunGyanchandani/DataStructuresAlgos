class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def sortedMerge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode(-1)  # Dummy node for easy merging
        curr = dummy

        while head1 and head2:
            if head1.data <= head2.data:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next  # Move the merged list pointer

        # Append the remaining nodes from the non-empty list
        curr.next = head1 if head1 else head2

        return dummy.next  # Return the merged list

# **Helper function to create a linked list from a list**
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# **Helper function to print linked list**
def printLinkedList(head):
    res = []
    while head:
        res.append(str(head.data))
        head = head.next
    print(" -> ".join(res))

# **Example usage**
sol = Solution()
head1 = createLinkedList([5, 10, 15, 40])
head2 = createLinkedList([2, 3, 20])
merged_head = sol.sortedMerge(head1, head2)
printLinkedList(merged_head)  # Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40

head1 = createLinkedList([1, 1])
head2 = createLinkedList([2, 4])
merged_head = sol.sortedMerge(head1, head2)
printLinkedList(merged_head)  # Output: 1 -> 1 -> 2 -> 4
