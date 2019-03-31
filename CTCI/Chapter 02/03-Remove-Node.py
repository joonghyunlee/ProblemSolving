class ListNode:
    def __init__(self, x=None):
        self.next = None
        self.val = x

class Solution:
    def remove(self, p):
        p.val = p.next.val
        p.next = p.next.next

    def convert_to_list(self, nums):
        curr = dummy = ListNode()
        for n in nums:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next

    def print_list(self, head):
        p = head
        while p:
            print p.val,
            p = p.next
        print


if __name__ == '__main__':
    s = Solution()
    head = s.convert_to_list([4, 5, 6, 7, 8])
    s.print_list(head)
    p = head.next.next.next
    s.remove(p)
    s.print_list(head)