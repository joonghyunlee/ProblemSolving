class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u',
                     'A', 'E', 'I', 'O', 'U']:
                stack.append(c)
        rev = []
        for i, c in enumerate(s):
            if c in ['a', 'e', 'i', 'o', 'u',
                     'A', 'E', 'I', 'O', 'U']:
                rev.append(stack.pop())
            else:
                rev.append(c)
        return ''.join(rev)


if __name__ == '__main__':
    s = Solution()
    r = s.reverseVowels('hello')
    print(r)
    r = s.reverseVowels('leetcode')
    print(r)
    r = s.reverseVowels('aA')
    print(r)
