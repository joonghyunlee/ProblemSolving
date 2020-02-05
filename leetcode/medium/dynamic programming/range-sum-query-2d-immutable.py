class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        self.matrix = matrix

        for i in range(n):
            for j in range(m):
                ul = self.getItem(i - 1, j - 1)
                bl = self.getItem(i, j - 1)
                ur = self.getItem(i - 1, j)
                self.matrix[i][j] += (bl + ur - ul)

    def getItem(self, row, col):
        return self.matrix[row][col] if row >= 0 and col >= 0 else 0
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ul = self.getItem(row1 - 1, col1 - 1)
        ur = self.getItem(row1 - 1, col2)
        bl = self.getItem(row2, col1 - 1)
        br = self.getItem(row2, col2)

        return br - ur - bl + ul


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    nm = NumMatrix(matrix)
    print nm.sumRegion(2, 1, 4, 3)
    print nm.sumRegion(1, 1, 2, 2)
    print nm.sumRegion(1, 2, 2, 4)

    matrix = [
        [-4, -5]
    ]
    nm = NumMatrix(matrix)
    print nm.sumRegion(0, 0, 0, 0)
    print nm.sumRegion(0, 0, 0, 1)
    print nm.sumRegion(0, 1, 0, 1)