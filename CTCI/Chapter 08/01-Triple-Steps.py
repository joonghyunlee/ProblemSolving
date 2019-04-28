class Solution:
    def findSteps(self, n):
        s = [1, 2, 4]
        for _ in range(3, n):
            s.append(0)

        for i in range(3, n):
            s[i] = s[i - 1] + s[i - 2] + s[i - 3]
        return s[n - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.findSteps(4)
    print r
    r = s.findSteps(2)
    print r
