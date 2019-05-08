class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = []
        for j in range(n):
            row = []
            for i in range(m):
                if j == 0:
                    row.append(1)
                elif i == 0:
                    row.append(1)
                else:
                    v = paths[j - 1][i] + row[i - 1]
                    row.append(v)
            paths.append(row)
        return paths[n - 1][m - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.uniquePaths(7, 3)
    print(r)
