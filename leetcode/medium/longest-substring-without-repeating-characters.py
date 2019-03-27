class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mdic = {}
        m, ms = 0, []
        for i, c in enumerate(s):
            pos =  mdic.get(c, -1)
            if pos < 0 or pos < i - m:
                mdic[c] = i
                m += 1
            elif pos >= i - m:
                mdic[c] = i
                ms.append(m)
                m = i - (pos + 1) + 1
        ms.append(m)
        return max(ms) if ms else 0


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring('abcabcbb')
    print r
    r = s.lengthOfLongestSubstring('bbbbb')
    print r
    r = s.lengthOfLongestSubstring('pwwkew')
    print r
    r = s.lengthOfLongestSubstring(' ')
    print r
    r = s.lengthOfLongestSubstring('')
    print r
    r = s.lengthOfLongestSubstring('aab')
    print r
    r = s.lengthOfLongestSubstring('dvdf')
    print r
    r = s.lengthOfLongestSubstring('tmmzuxt')
    print r
