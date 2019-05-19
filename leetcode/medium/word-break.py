class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        n, m = len(s), [0] * len(s)
        for i in range(n):
            if i != 0 and m[i - 1] == 0:
                continue
            for w in wordDict:
                l = len(w)
                if i+l-1 < n and s[i:i+l] == w:
                    m[i+l-1] = 1
        return True if m and m[-1] else False


if __name__ == '__main__':
    so = Solution()
    s = 'leetcode'
    wordDict = [
        'leet',
        'code'
    ]
    r = so.wordBreak(s, wordDict)
    print(r)
