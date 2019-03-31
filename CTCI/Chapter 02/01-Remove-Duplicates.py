class ListNode:
    def __init__(self, x=None):
        self.next = None
        self.val = x

class Solution:
    def __init__(self):
        self.cdict = {}

    def find_duplicate(self, head):
        curr = dummy = ListNode()
        dummy.next = head

        while curr.next:
            freq = self.cdict.get(curr.next.val, 0)
            if freq <= 0:
                self.cdict[curr.next.val] = freq + 1
                curr = curr.next
            else:
                curr.next = curr.next.next
        return dummy.next

    def convert_to_list(self, msg):
        curr = dummy = ListNode()
        for c in msg:
            curr.next = ListNode(c)
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
    head = s.convert_to_list('follow')
    s.print_list(head)
    r = s.find_duplicate(head)
    s.print_list(r)