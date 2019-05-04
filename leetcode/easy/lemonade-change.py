class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        def withdraw(a, b):
            if a[b] > 0:
                a[b] -= 1
                return b
            return -1

        a = {5: 0, 10: 0, 20: 0}
        ks = [20, 10, 5]
        for b in bills:
            a[b] += 1
            c, i = (b - 5), 0
            while c > 0:
                if i > 2:
                    return False
                if ks[i] > c:
                    i += 1
                    continue
                d = withdraw(a, ks[i])
                if d < 0:
                    i += 1
                    continue
                c -= d
            print a
            print c
        return True


if __name__ == '__main__':
    s = Solution()
    bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
    r = s.lemonadeChange(bills)
    print(r)
