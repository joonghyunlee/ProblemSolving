class Solution(object):
    def longestPalindromeBruteForce(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            return True if s == s[::-1] else False

        mp, ms = (0, 0), 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j]) and ms < (j - i + 1):
                    mp, ms = (i, j), j - i + 1

        return s[mp[0]:mp[1]]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pmap = [[False for end in range(len(s))] for start in range(len(s))]
        candidates = [(-1, -1)]
        for length in range(1, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if length == 1:
                    pmap[start][end] = True
                    candidates.append((start, end))
                elif length == 2:
                    if s[start] == s[end]:
                        pmap[start][end] = True
                        candidates.append((start, end))
                else:
                    if pmap[start + 1][end - 1] and s[start] == s[end]:
                        pmap[start][end] = True
                        candidates.append((start, end))

        start, end = candidates.pop()
        return s[start:end + 1] if start >=0 and end >= 0 else ""


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome('babad')
    print r
    r = s.longestPalindrome('aaaa')
    print r
