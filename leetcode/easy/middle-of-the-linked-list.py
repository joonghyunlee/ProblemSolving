# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(self, nums):
        p = head = ListNode(None)
        for n in nums:
            p.next = ListNode(n)
            p = p.next
        return head.next


# 1 - 2 - 3 - 4 - 5
# 1 - 2 - 3 - 4 - 5 - 6
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = f = head
        c = 1
        p = head
        while f.next:
            c += 1
            if c % 2 == 0:
                s = s.next
            f = f.next

        return s


if __name__ == '__main__':
    s = Solution()
    head = ListNode.from_list([1, 2, 3, 4, 5, 6])
    r = s.middleNode(head)
    print r
    head = ListNode.from_list([1, 2, 3, 4, 5, 6, 7])
    r = s.middleNode(head)
    print r
