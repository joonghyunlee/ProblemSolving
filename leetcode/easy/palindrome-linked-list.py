# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []; queue = []
        p = head; c = 0
        while p:
            stack.append(p.val)
            queue.insert(0, p.val)
            c += 1
            p = p.next

        for i in range(c // 2):
            if stack.pop() != queue.pop():
                return False
        return True

    def convertToList(self, nums):
        if not nums:
            return None
        head = ListNode(nums[0])
        p = head
        for n in nums[1:]:
            p.next = ListNode(n)
            p = p.next
        return head


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    h = s.convertToList(nums)
    print(s.isPalindrome(h))
    nums = [1,2,2,1]
    h = s.convertToList(nums)
    print(s.isPalindrome(h))
    nums = [1,2,3,2,1]
    h = s.convertToList(nums)
    print(s.isPalindrome(h))
    nums = [1]
    h = s.convertToList(nums)
    print(s.isPalindrome(h))
