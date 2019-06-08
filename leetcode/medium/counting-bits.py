class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        for n in range(1, num + 1):
            ret.append(ret[n >> 1] + (n & 1))

        return ret


if __name__ == '__main__':
    s = Solution()
    r = s.countBits(20)
    print r
