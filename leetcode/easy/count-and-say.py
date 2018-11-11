class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def sequence(l):
            target = l[0]
            count = 0
            new = []
            for i in l:
                if target == i:
                    count += 1
                else:
                    new.append(count)
                    new.append(target)
                    target = i
                    count = 1

            if count:
                new.append(count)
                new.append(target)
            return new

        seq = [1]
        for i in range(n - 1):
            seq = sequence(seq)

        return ''.join([str(i) for i in seq])


if __name__ == '__main__':
    s = Solution()
    r = s.countAndSay(1)
    print r
    r = s.countAndSay(4)
    print r
    r = s.countAndSay(6)
    print r
