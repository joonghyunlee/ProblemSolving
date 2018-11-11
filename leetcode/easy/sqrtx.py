class Solution(object):
    def mySqrt(self, x):
        r = x // 2
        d = x
        while r**2 != x:
            if r**2 < x and ((r+1) ** 2) > x:
                break
            d = d // 2 if d > 1 else 1
            if (r**2) < x:
                r += d
            elif (r**2) > x:
                r -= d
        return r


if __name__ == '__main__':
    s = Solution()
    r = s.mySqrt(4)
    print(r)
    r = s.mySqrt(8)
    print(r)
    r = s.mySqrt(1)
    print(r)
    r = s.mySqrt(100)
    print(r)
    r = s.mySqrt(2147395599)
    print(r)
