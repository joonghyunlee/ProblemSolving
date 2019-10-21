# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def from_list(cls, nums):
        tail = head = cls(None)
        for num in nums:
            tail.next = cls(num)
            tail = tail.next
        return head.next

    @classmethod
    def iterator(cls, p):
        while p is not None:
            yield p
            p = p.next

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def insert(heap, n):
            heap.append(n)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[i].val < heap[p].val:
                    heap[i], heap[p] = heap[p], heap[i]
                    i = p
                else:
                    break

        def heapify(heap, i):
            l, r = 2 * i + 1, 2 * i + 2
            smallest = i
            if l <= len(heap) - 1 and heap[l].val < heap[smallest].val:
                smallest = l
            if r <= len(heap) - 1 and heap[r].val < heap[smallest].val:
                smallest = r

            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                heapify(heap, smallest)

        ps = []
        for lh in lists:
            if lh is not None:
                insert(ps, lh)

        head = ListNode(None)
        tail = head

        while ps:
            ps[0], ps[len(ps) - 1] = ps[len(ps) - 1], ps[0]
            minp = ps.pop()
            heapify(ps, 0)

            if minp.next is not None:
                insert(ps, minp.next)

            tail.next = minp
            tail = tail.next

        return head.next


if __name__ == '__main__':
    s = Solution()
    lists = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6])
    ]
    r = s.mergeKLists(lists)
    for v in ListNode.iterator(r):
        print v,
    print
    r = s.mergeKLists([
        None
    ])
    for v in ListNode.iterator(r):
        print v,
    print
    r = s.mergeKLists([
        ListNode(1), ListNode(0)
    ])
    for v in ListNode.iterator(r):
        print v,
    print
    r = s.mergeKLists([
        ListNode.from_list([-8, -7, -6, -3, -2, -2, 0, 3]),
        ListNode.from_list([-10, -6, -4, -4, -4, -2, -1, 4]),
        ListNode.from_list([-10, -9, -8, -8, -6]),
        ListNode.from_list([-10, 0, 4])
    ])
    for v in ListNode.iterator(r):
        print v,
    print
    r = s.mergeKLists([
        ListNode.from_list([-6,-3,-1,1,2,2,2]),
        ListNode.from_list([-10,-8,-6,-2,4]),
        ListNode.from_list([-2]),
        ListNode.from_list([-8,-4,-3,-3,-2,-1,1,2,3]),
        ListNode.from_list([-8,-6,-5,-4,-2,-2,2,4])
    ])
    for v in ListNode.iterator(r):
        print v,
    print
    r = s.mergeKLists([
        ListNode.from_list([-8,-7,-7,-5,1,1,3,4]),
        ListNode.from_list([-2]),
        ListNode.from_list([-10,-10,-7,0,1,3]),
        ListNode.from_list([2])
    ])
    for v in ListNode.iterator(r):
        print v,
    print
    r = s.mergeKLists([
        ListNode.from_list([-8,-7,-6,-3,-2,-2,0,3]),
        ListNode.from_list([-10,-6,-4,-4,-4,-2,-1,4]),
        ListNode.from_list([-10,-9,-8,-8,-6]),
        ListNode.from_list([-10,0,4])
    ])
    for v in ListNode.iterator(r):
        print v,
    print
