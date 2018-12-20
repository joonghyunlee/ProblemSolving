class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sdic, tdic = {}, {}
        for c in s:
            sdic[c] = sdic.get(c, 0) + 1
        for c in t:
            tdic[c] = tdic.get(c, 0) + 1

        for k, v in tdic.items():
            if sdic.get(k, 0) != v:
                return k
        return None


if __name__ == '__main__':
    s = Solution()
    r = s.findTheDifference('abcd', 'abcde')
    print(r)
    r = s.findTheDifference('aaa', 'aaaa')
    print(r)
