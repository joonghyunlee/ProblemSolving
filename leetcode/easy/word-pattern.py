class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        tokens = str.split()
        if len(pattern) != len(tokens):
            return False

        for i, token in enumerate(tokens):
            p = pattern[i]
            val = dic.get(p, None)
            if not val:
                dic[p] = token
            elif val != token:
                return False
        if len(set(dic.values())) != len(dic.keys()):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.wordPattern('abba', 'dog cat cat dog')
    print r
    r = s.wordPattern('abba', 'dog cat cat fish')
    print r
    r = s.wordPattern('aaaa', 'dog cat cat dog')
    print r
    r = s.wordPattern('abba', 'dog dog dog dog')
    print r
