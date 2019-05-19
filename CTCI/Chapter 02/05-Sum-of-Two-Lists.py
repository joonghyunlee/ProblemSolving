class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = [self.val]
        p = self.next
        while p:
            s.insert(0, p.val)
            p = p.next
        return ''.join(map(lambda x: str(x), s))

    @classmethod
    def from_int(cls, num):
        p = head = ListNode(None)
        while num:
            p.next = ListNode(num % 10)
            p = p.next
            num //= 10
        return head.next


class Solution:
    def sum(self, a, b):
        pa, pb = a, b
        carry = 0
        p = head = ListNode(None)
        while pa or pb:
            s = 0
            if pa:
                s += pa.val
                pa = pa.next
            if pb:
                s += pb.val
                pb = pb.next

            if carry > 0:
                s += carry
                carry = 0
            if s >= 10:
                s = s - 10
                carry = 1
            p.next = ListNode(s)
            p = p.next
        if carry:
            p.next = ListNode(carry)
        return head.next


if __name__ == '__main__':
    s = Solution()
    a = ListNode.from_int(123617)
    print a
    b = ListNode.from_int(395)
    print b
    r = s.sum(a, b)
    print r
