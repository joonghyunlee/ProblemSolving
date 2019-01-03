class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for c in s:
            m[c] = m.setdefault(c, 0) + 1

        longest = 0
        odd = 0
        for v in sorted(m.values(), reverse=True):
            if v % 2 == 0:
                longest += v
            elif v % 2 == 1 and v != 1:
                odd = 1
                longest += v - 1
            elif v == 1:
                odd = 1
                break
        return longest + odd


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome('abccccdd')
    print(r)
    r = s.longestPalindrome('ccccddeee')
    print(r)
    r = s.longestPalindrome('ccccdde')
    print(r)
