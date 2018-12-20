def guess(num):
    global target
    if num > target:
        return -1
    elif num < target:
        return 1
    return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m
            elif guess(m) == 1:
                l = m + 1
        return r


if __name__ == '__main__':
    import random
    target = random.randint(0, 10)
    print(target)
    s = Solution()
    r = s.guessNumber(10)
    print(r)
