class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s:
            return 0
        g.sort()
        s.sort()
        i, j, c = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                c += 1
                i += 1
            j += 1
        return c


if __name__ == '__main__':
    so = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    r = so.findContentChildren(g, s)
    print(r)
