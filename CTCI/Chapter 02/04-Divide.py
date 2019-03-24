class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def divide(head, x):
    dummy_head, tail_head = ListNode(None), None
    dummy_head.next = head

    p = dummy_head
    while p.next:
        if p.next.val >= x:
            target = p.next
            p.next = p.next.next
            target.next = tail_head
            tail_head = target
        else:
            p = p.next

    p.next = tail_head
    return dummy_head.next


def convertToList(nums):
    p = head = ListNode(None)
    for n in nums:
        p.next = ListNode(n)
        p = p.next
    head = head.next
    return head


def printList(head):
    p = head

    while p:
        print p.val,
        p = p.next


if __name__ == '__main__':
    head = convertToList([9, 5, 8, 5, 10, 2, 1])
    r = divide(head, 5)
    printList(r)
