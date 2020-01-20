# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next

        tp = p = stack.pop()
        while p != head:
            p.next = stack.pop()
            p = p.next

        p.next = None

        return tp

    def reverseList2(self, head):
        def recursion(node):
            if not node.next:
                return node, node
            
            prev, tail = recursion(node.next)
            prev.next = node
                
            return node, tail
        
        if not head:
            return None
        
        tail, head = recursion(head)
        tail.next = None
        
        return head

    def toLinkedList(self, nums):
        h = ListNode(0)
        p = h
        for n in nums:
            p.next = ListNode(n)
            p = p.next
        h = h.next
        return h

    def printLinkedList(self, head):
        p = head
        while p:
            print p.val,
            p = p.next
        print


if __name__ == '__main__':
    s = Solution()
    head = s.toLinkedList([1, 2, 3, 4, 5])
    r = s.reverseList2(head)
    s.printLinkedList(r)
    head = s.toLinkedList([])
    r = s.reverseList2(head)
    s.printLinkedList(r)
