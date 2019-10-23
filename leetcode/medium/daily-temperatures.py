class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        forecast = [0] * len(T)
        for i, t in enumerate(T):
            while stack:
                pi, pt = stack.pop()
                if pt >= t:
                    stack.append((pi, pt))
                    break
                forecast[pi] = i - pi
            stack.append((i, t))

        return forecast


if __name__ == '__main__':
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    r = s.dailyTemperatures(T)
    print r
    T = [14]
    r = s.dailyTemperatures(T)
    print r