class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sd = {}
        for i in range(len(s)):
            d = sd.get(s[i], None)
            if not d:
                if t[i] in sd.values():
                    return False
                sd[s[i]] = t[i]
            elif d != t[i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isIsomorphic('egg', 'add')
    print r
    r = s.isIsomorphic('foo', 'bar')
    print r
    r = s.isIsomorphic('paper', 'title')
    print r
    r = s.isIsomorphic('aria', 'vacvd')
    print r
    r = s.isIsomorphic('a', 't')
    print r
    r = s.isIsomorphic('ab', 'aa')
    print r
