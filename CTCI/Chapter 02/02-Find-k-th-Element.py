class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find1(head, k):
    q = []
    p = head

    while p:
        if len(q) == k:
            q.pop()
        q.insert(0, p)
        p = p.next

    return q.pop() if len(q) == k else None


def find2(head, k):
    slow, fast = head, head
    diff = 0

    while fast:
        if diff == k:
            slow = slow.next
        else:
            diff += 1
        fast = fast.next

    return slow if diff == k else None


if __name__ == '__main__':
    head = ListNode(10)
    head.next = ListNode(9)
    head.next.next = ListNode(8)
    head.next.next.next = ListNode(7)

    r = find1(head, 2)
    if r:
        print r.val

    r = find2(head, 2)
    if r:
        print r.val
