class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def helper(r, c, oldColor, newColor):
            if oldColor == newColor:
                return
            if image[r][c] != oldColor:
                return

            image[r][c] = newColor

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if not (0 <= r + dr < len(image)):
                    continue
                elif not (0 <= c + dc < len(image[0])):
                    continue

                if image[r + dr][c + dc] == oldColor:
                    helper(r + dr, c + dc, oldColor, newColor)

        helper(sr, sc, image[sr][sc], newColor)
        return image


if __name__ == '__main__':
    s = Solution()
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    print s.floodFill(image, 1, 1, 2)
    image = [
        [0, 0, 0],
        [0, 1, 1]
    ]
    print s.floodFill(image, 1, 1, 1)