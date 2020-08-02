class Solution:
    def isRectangleCover(self, rectangles: 'List[List[int]]') -> bool:
        def bottomLeft(rect):
            return (rect[0], rect[1])

        def topLeft(rect):
            return (rect[2], rect[1])

        def bottomRight(rect):
            return (rect[0], rect[3])

        def topRight(rect):
            return (rect[2], rect[3])

        if not rectangles:
            return False

        minBottom, minLeft = float("inf"), float("inf")
        maxTop, maxRight = -float("inf"), -float("inf")

        area = 0
        coordSet = set()
        for rect in rectangles:
            minBottom, minLeft = min(rect[0], minBottom), min(rect[1], minLeft)
            maxTop, maxRight = max(rect[2], maxTop), max(rect[3], maxRight)

            area += (rect[2] - rect[0]) * (rect[3] - rect[1])

            if bottomLeft(rect) in coordSet:
                coordSet.remove(bottomLeft(rect))
            else:
                coordSet.add(bottomLeft(rect))
            if bottomRight(rect) in coordSet:
                coordSet.remove(bottomRight(rect))
            else:
                coordSet.add(bottomRight(rect))
            if topLeft(rect) in coordSet:
                coordSet.remove(topLeft(rect))
            else:
                coordSet.add(topLeft(rect))
            if topRight(rect) in coordSet:
                coordSet.remove(topRight(rect))
            else:
                coordSet.add(topRight(rect))

        if (minBottom, minLeft) not in coordSet:
            return False
        if (minBottom, maxRight) not in coordSet:
            return False
        if (maxTop, minLeft) not in coordSet:
            return False
        if (maxTop, maxRight) not in coordSet:
            return False

        if len(coordSet) != 4:
            return False

        return area == (maxTop - minBottom) * (maxRight - minLeft)


if __name__ == '__main__':
    s = Solution()
    rectangles = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]
    r = s.isRectangleCover(rectangles)
    print(r)
    rectangles = [
        [1, 1, 2, 3],
        [1, 3, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 4, 4]
    ]
    r = s.isRectangleCover(rectangles)
    print(r)
    rectangles = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [3, 2, 4, 4]
    ]
    r = s.isRectangleCover(rectangles)
    print(r)
    rectangles = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [2, 2, 4, 4]
    ]
    r = s.isRectangleCover(rectangles)
    print(r)
    rectangles = [
        [0, 0, 2, 2],
        [1, 1, 3, 3],
        [2, 0, 3, 1],
        [0, 3, 3, 4]
    ]
    r = s.isRectangleCover(rectangles)
    print(r)
