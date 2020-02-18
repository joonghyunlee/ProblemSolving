class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence2(self, s, t):
        # create a map
        tMap = dict()
        for i, c in enumerate(t):
            v = tMap.get(c, list())
            v.append(i)
            tMap[c] = v
        
        from bisect import bisect_left
        low = 0     # minimum index
        for c in s:
            if c not in tMap:
                return False
            indexList = tMap[c]
            # find an index that is larger than or equal to low
            i = bisect_left(indexList, low)
            if i == len(indexList):
                return False
            low = indexList[i] + 1
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isSubsequence('abc', 'ahbgdc')
    print r
    r = s.isSubsequence2('abc', 'ahbgdc')
    print r
    r = s.isSubsequence('abc', 'ahcbgd')
    print r
    r = s.isSubsequence2('abc', 'ahcbgd')
    print r
    r = s.isSubsequence('axc', 'ahbgdc')
    print r
    r = s.isSubsequence2('axc', 'ahbgdc')
    print r