class Solution:
    def findMinArrowsShots(self, points):
        points.sort()
        arrows, shots = 0, 0
        start, end = 0, float('inf')
        for next_start, next_end in points:
            if next_start <= end:
                shots += 1
                start = next_start
                end = min(end, next_end)
            else:
                arrows += 1 if shots > 0 else 0
                shots = 1
                start = next_start
                end = next_end
        arrows += 1 if shots > 0 else 0
        return arrows
        
        
if __name__ == '__main__':
    s = Solution()
    points = [[10,16], [2,8], [1,6], [7,12]]
    r = s.findMinArrowsShots(points)
    print(r)