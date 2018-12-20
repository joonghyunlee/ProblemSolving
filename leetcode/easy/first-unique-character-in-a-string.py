class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cdict = dict()
        for i, c in enumerate(s):
            v = cdict.get(c, None)
            cdict[c] = i if v is None else len(s)

        min = len(s)
        for k in cdict.keys():
            if cdict[k] < min:
                min = cdict[k]

        return min if min < len(s) else -1


if __name__ == '__main__':
    s = Solution()
    r = s.firstUniqChar('leetcode')
    print(r)
    r = s.firstUniqChar('loveleetcode')
    print(r)
    r = s.firstUniqChar('cc')
    print(r)
