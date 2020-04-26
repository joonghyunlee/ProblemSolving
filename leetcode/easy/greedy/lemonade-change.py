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
        return True

    def lemonadeChange2(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        charges = {c: 0 for c in [5, 10]}
        for bill in bills:
            if bill == 5:
                charges[5] += 1
            elif bill == 10:
                if charges[5] > 0:
                    charges[5] -= 1
                    charges[10] += 1
                else:
                    return False
            else:
                if charges[10] > 0 and charges[5] > 0:
                    charges[10] -= 1
                    charges[5] -= 1
                elif charges[5] >= 3:
                    charges[5] -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
    r = s.lemonadeChange(bills)
    print(r)
    r = s.lemonadeChange2(bills)
    print(r)
