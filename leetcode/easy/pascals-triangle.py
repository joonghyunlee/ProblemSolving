class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        tri = [[1]]
        for i in range(numRows - 1):
            line = [0] * (i + 2)
            line[0] = line[i + 1] = 1
            for j in range(1, i + 1):
                line[j] = tri[i][j-1] + tri[i][j]
            tri.append(line)

        return tri


if __name__ == '__main__':
    s = Solution()
    r = s.generate(5)
    print r
    r = s.generate(1)
    print r
    r = s.generate(2)
    print r
    r = s.generate(12)
    print r
