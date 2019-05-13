class Solution(object):
    def compare(self, a, b):
        la, lb = len(a), len(b)
        if abs(la - lb) > 1:
            return False

        i, j = 0, 0
        count = 0

        while i < la and j < lb:
            if count > 1:
                return False

            if a[i] != b[j]:
                count += 1
                if la > lb:
                    i += 1
                elif la < lb:
                    j += 1

            i += 1
            j += 1

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.compare('pale', 'bale')
    print r
