class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        convs = {}
        for i in range(len(s) - 9):
            conv = 0
            for j in range(10):
                conv |= 'ACGT'.index(s[i + j])
                conv <<= 2
            v = convs.setdefault(conv, [])
            v.append(i)

        resp = []
        for k, v in convs.items():
            if len(v) > 1:
                resp.append(s[v[0]:v[0] + 10])
        return resp


if __name__ == '__main__':
    so = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    r = so.findRepeatedDnaSequences(s)
    print r
