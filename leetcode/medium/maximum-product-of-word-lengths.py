class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bits = []
        for w in words:
            m = 0
            for c in w:
                m |= 1 << ord(c) - ord('a')
            bits.append(m)
        ret = [0]
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if bits[i] & bits[j] == 0:
                    ret.append(len(words[i]) * len(words[j]))
        return max(ret)


if __name__ == '__main__':
    s = Solution()
    r = s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print r
