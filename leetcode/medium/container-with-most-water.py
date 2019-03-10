class Solution(object):
    def maxArea(self, height):
        def calc(i, j):
            return (j - i) * min(height[i], height[j])

        maxArea = 0
        left, right = 0, len(height) - 1

        while left < right:
            maxArea = max(maxArea, calc(left, right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    r = s.maxArea(height)
    print r
    height = [3, 2, 1, 3]
    r = s.maxArea(height)
    print r
