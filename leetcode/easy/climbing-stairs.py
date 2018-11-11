class Solution(object):
    def climbStairs(self, n):
        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n-1]


if __name__ == '__main__':
    s = Solution()
    r = s.climbStairs(4)
    print(r)
