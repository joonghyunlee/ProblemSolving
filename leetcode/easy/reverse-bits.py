class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = 0
        c = 0
        while c < 32:
            s *= 2
            s += (n % 2)
            n //= 2
            c += 1
        return s


if __name__ == '__main__':
    s = Solution()
    r = s.reverseBits(43261596)
    print r
