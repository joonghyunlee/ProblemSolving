class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        cnt = [0] * 26
        maxLen = 0
        for i in range(n):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or
                (p[i - 1] == 'z' and p[i] == 'a')):
                maxLen += 1
            else:
                maxLen = 1
            idx = ord(p[i]) - ord('a')
            cnt[idx] = max(cnt[idx], maxLen)

        total = 0
        for i in range(26):
            total += cnt[i]

        return total


if __name__ == '__main__':
    s = Solution()
    r = s.findSubstringInWraproundString('abcdzzffffazbcdefoijujmascccccdflvnxc')
    print r
    r = s.findSubstringInWraproundString('cac')
    print r
    r = s.findSubstringInWraproundString('zab')
    print r
