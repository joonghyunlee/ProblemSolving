class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        row = []
        for j in range(rowIndex):
            new_row = []
            for i in range(j):
                new_row.append(row[i] + row[i + 1])
            new_row.insert(0, 1)
            new_row.append(1)
            row = new_row

        return row


if __name__ == '__main__':
    s = Solution()
    r = s.getRow(0)
    print r
    r = s.getRow(1)
    print r
    r = s.getRow(2)
    print r
    r = s.getRow(3)
    print r
    r = s.getRow(4)
    print r
    r = s.getRow(5)
    print r
    r = s.getRow(6)
    print r
