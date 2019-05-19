class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def length(self):
        p, c = self.next, 1
        while p:
            p = p.next
            c += 1
        return c

    @classmethod
    def from_list(cls, nums):
        p = head = cls(None)
        for n in nums:
            p.next = cls(n)
            p = p.next
        return head.next


class Solution():
    def intersection(self, a, b):
        pa, pb = a, b

        la, lb = a.length(), b.length()
        ldiff = abs(la - lb)
        if la > lb:
            for _ in range(ldiff):
                pa = pa.next
        elif lb > la:
            for _ in range(ldiff):
                pb = pb.next

        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None


if __name__ == '__main__':
    s = Solution()
    a = ListNode.from_list([1, 2, 3])
    b = ListNode.from_list([1, 2, 3, 4, 5, 6])
    c = ListNode.from_list([7, 8, 9])
    pa, pb = a, b
    while pa.next:
        pa = pa.next
    while pb.next:
        pb = pb.next
    pa.next, pb.next = c, c

    r = s.intersection(a, b)
    print r

    a = ListNode.from_list([1, 2, 3])
    b = ListNode.from_list([1, 2, 3, 4, 5, 6])
    r = s.intersection(a, b)
    print r
