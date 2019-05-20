class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def from_list(cls, items):
        p = root = cls(None)
        for i in items:
            p.next = cls(i)
            p = p.next
        return root.next


class Comparator(object):
    def compare(self, a):
        s = []
        l = 0
        p = a
        while p:
            s.append(p)
            p = p.next
            l += 1

        p = a
        for _ in range(l // 2):
            n1 = s.pop()
            if n1.val != p.val:
                return False
            p = p.next

        return True


if __name__ == '__main__':
    comp = Comparator()
    a = ListNode.from_list(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    print comp.compare(a)
    a = ListNode.from_list(['a', 'b', 'c', 'c', 'b', 'a'])
    print comp.compare(a)
    a = ListNode.from_list(['a', 'b', 'd', 'c', 'b', 'a'])
    print comp.compare(a)
