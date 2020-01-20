# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, nums):
        nodes = []
        for i, num in enumerate(nums):
            node = cls(num)
            if i > 0:
                nodes[i - 1].next = node
            nodes.append(node)
        return nodes[0] if nodes else None

    @classmethod
    def print_list(cls, head):
        node = head
        while node:
            print node,
            node = node.next
        print


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack, queue = [], []
        node = head
        while node:
            stack.append(node)
            queue.insert(0, node)
            node = node.next

        i, n = 0, len(queue)
        node = head = ListNode(None)
        while i < (n // 2):
            node.next = queue.pop()
            node = node.next
            node.next = stack.pop()
            node = node.next
            i += 1

        if n % 2 == 1:
            node.next = queue.pop()
            node = node.next
        node.next = None

        return head.next

    def reorderList2(self, head):
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        i, n = 0, len(nodes)
        li, ri = 0, n - 1
        node = head = ListNode(None)
        while i < (n // 2):
            node.next = nodes[li]
            node = node.next
            node.next = nodes[ri]
            node = node.next
            i += 1
            li += 1
            ri -= 1
        if n % 2 == 1:
            node.next = nodes[li]
            node = node.next
        node.next = None

        return head.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode.from_list([1, 2, 3, 4])
    r = s.reorderList2(head)
    ListNode.print_list(r)
    head = ListNode.from_list([1, 2, 3, 4, 5])
    r = s.reorderList2(head)
    ListNode.print_list(r)
    head = ListNode.from_list([1])
    r = s.reorderList2(head)
    ListNode.print_list(r)
    head = ListNode.from_list([])
    r = s.reorderList2(head)
    ListNode.print_list(r)
