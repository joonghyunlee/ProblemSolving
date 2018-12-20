class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # make a dictionary by magazine
        mdic = dict()
        for c in magazine:
            mdic[c] = mdic.get(c, 0) + 1

        # scan ransomeNote
        for c in ransomNote:
            mdic[c] = mdic.get(c, 0) - 1

        # aggregate
        for v in mdic.values():
            if v < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.canConstruct('a', 'b')
    print(r)
    r = s.canConstruct('aa', 'ab')
    print(r)
    r = s.canConstruct('aa', 'aab')
    print(r)
