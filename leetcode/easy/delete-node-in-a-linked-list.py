# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        while True:
            n = p.next
            if n:
                p.val = n.val
                nn = n.next
                if not nn:
                    break
            p = n
        p.next = None

    def convertToList(self, nums):
        if not nums:
            return None
        head = ListNode(nums[0])
        p = head
        for n in nums[1:]:
            p.next = ListNode(n)
            p = p.next
        return head

    def printList(self, head):
        p = head
        while p:
            print p.val,
            p = p.next
        print


if __name__ == '__main__':
    s = Solution()
    head = s.convertToList([4, 5, 1, 9])
    s.deleteNode(head.next)
    s.printList(head)
    head = s.convertToList([4, 5, 1, 9])
    s.deleteNode(head.next.next)
    s.printList(head)


