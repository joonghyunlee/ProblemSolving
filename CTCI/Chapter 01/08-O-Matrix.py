class Solution:
    def cross(self, m):
        rows = []
        cols = []
        for r in range(len(m)):
            for c in range(len(m[0])):
                if m[r][c] == 0:
                    rows.append(r)
                    cols.append(c)
        for r in range(len(m)):
            for c in range(len(m[0])):
                if r in rows or c in cols:
                    m[r][c] = 0

    def cross2(self, m):
        first_row_has_zero = False
        first_col_has_zero = False

        for r in range(len(m)):
            if m[r][0] == 0:
                first_col_has_zero = True
                break

        for c in range(len(m[0])):
            if m[0][c] == 0:
                first_row_has_zero = True
                break

        for r in range(1, len(m)):
            for c in range(1, len(m[0])):
                if m[r][c] == 0:
                    m[r][0] = 0
                    m[0][c] = 0

        for r in range(1, len(m)):
            for c in range(1, len(m[0])):
                if m[r][0] == 0 or m[0][c] == 0:
                    m[r][c] = 0

        if first_col_has_zero:
            for r in range(len(m)):
                m[r][0] = 0

        if first_row_has_zero:
            for c in range(len(m[0])):
                m[0][c] = 0


if __name__ == '__main__':
    s = Solution()
    m = [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]
    ]
    s.cross2(m)
    print m
