class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        p = reduce(lambda x, y: x * y, range(1, n)) if n > 1 else 1
        ret = []
        k -= 1
        while k > 0:
            if k < p:
                ret.append(nums.pop(0))
            else:
                ret.append(nums.pop(k // p))
                k %= p
            n -= 1
            p //= n

        ret.extend(nums)

        return ''.join(ret)


if __name__ == '__main__':
    s = Solution()
    r = s.getPermutation(3, 2)
    print r
    r = s.getPermutation(3, 4)
    print r
    r = s.getPermutation(4, 9)
    print r
    r = s.getPermutation(1, 1)
    print r
