class Solution:
    def compress(self, s):
        n, c = len(s), 1
        comp = []
        for i in range(1, n + 1):
            if i == n or s[i - 1] != s[i]:
                comp.append(s[i - 1])
                comp.append(str(c))
                c = 1
            else:
                c += 1

        if n < len(comp):
            return s
        return ''.join(comp)


if __name__ == '__main__':
    s = Solution()
    r = s.compress('aabccccaaa')
    print r
    r = s.compress('abcd')
    print r
    r = s.compress('aaaabbbcccccd')
    print r
