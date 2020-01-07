class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def match(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                return match(s, l, r - 1) or match(s, l + 1, r)
            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
    print r
    r = s.validPalindrome('aba')
    print r
    r = s.validPalindrome('abca')
    print r
    r = s.validPalindrome('abcdedckba')
    print r
    r = s.validPalindrome('abc')
    print r