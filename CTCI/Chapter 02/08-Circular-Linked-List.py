class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def get(self, i):
        p = self
        for _ in range(i):
            p = p.next
        return p

    def tail(self):
        p = self.next
        while p.next:
            p = p.next
        return p

    @classmethod
    def from_list(self, nums):
        p = root = ListNode(None)
        for n in nums:
            p.next = ListNode(n)
            p = p.next
        return root.next


class Finder(object):
    def find(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast


if __name__ == '__main__':
    f = Finder()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = ListNode.from_list(nums)
    tail = head.tail()
    tail.next = head.get(4)
    r = f.find(head)
    print r
