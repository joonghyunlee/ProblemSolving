class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        l, r = min(start, destination), max(start, destination)
        clockwise = sum(distance[l:r])
        return min(clockwise, sum(distance) - clockwise)


if __name__ == '__main__':
    s = Solution()
    distance = [1, 2, 3, 4]
    r = s.distanceBetweenBusStops(distance, 0, 1)
    print r

    distance = [1, 2, 3, 4]
    r = s.distanceBetweenBusStops(distance, 0, 2)
    print r

    distance = [1, 2, 3, 4]
    r = s.distanceBetweenBusStops(distance, 0, 3)
    print r

    distance = [7, 10, 1, 12, 11, 14, 5, 0]
    r = s.distanceBetweenBusStops(distance, 7, 2)
    print r
