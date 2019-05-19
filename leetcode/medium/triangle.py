class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        m = 0
        paths = [triangle[0]]
        for d in range(1, len(triangle)):
            row = []
            paths.append(row)
            for i in range(d):
                l, r = i, i + 1
                lv = triangle[d][l] + paths[d-1][i]
                if not row:
                    row.append(lv)
                elif row and row[-1] > lv:
                    row.pop()
                    row.append(lv)

                row.append(triangle[d][r] + paths[d-1][i])
        return min(paths[-1])


if __name__ == '__main__':
    s = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    r = s.minimumTotal(triangle)
    print(r)
