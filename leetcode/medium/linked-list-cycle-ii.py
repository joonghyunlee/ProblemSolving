# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, nums):
        head = p = cls(None)
        for num in nums:
            p.next = cls(num)
            p = p.next
        return head.next, p

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def getCycleLength(p):
            cnt = 1
            sp, fp = p, p
            while sp and fp:
                fp = fp.next

                if sp == fp:
                    return cnt
                elif not fp:
                    break

                cnt += 1
                sp = sp.next
                fp = fp.next
            return 0

        def findStart(p, length):
            pos = 0
            fp = sp = p
            for _ in range(length):
                fp = fp.next

            while sp and fp:
                if fp == sp:
                    return fp
                pos += 1
                sp = sp.next
                fp = fp.next
            return None

        length = getCycleLength(head)
        if length == 0:
            return None

        return findStart(head, length)

if __name__ == '__main__':
    s = Solution()
    # 1 - 2 - 3 
    #     |___|
    head, tail = ListNode.from_list([1, 2, 3])
    tail.next = head.next
    r = s.detectCycle(head)
    print r
    # 3 - 2 - 0 - -4
    #     |________|
    head, tail = ListNode.from_list([3, 2, 0, -4])
    tail.next = head.next
    r = s.detectCycle(head)
    print r
    # 1 - 0
    # |___|
    head, tail = ListNode.from_list([1, 0])
    tail.next = head
    r = s.detectCycle(head)
    print r
    # 1
    # no cycle
    head, tail = ListNode.from_list([1])
    r = s.detectCycle(head)
    print r