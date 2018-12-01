class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))


if __name__ == '__main__':
    s = Solution()
    r = s.reverseString('hello')
    print r
    r = s.reverseString('A man, a plan, a canal: Panama')
    print r
