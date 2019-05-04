class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        D = []
        i = len(A[0]) - 1
        while i >= 0:
            prev = 'a'
            for s in A:
                if s[i] < prev:
                    D.append(i)
                    break
                else:
                    prev = s[i]
            i -= 1
        return len(D)


if __name__ == '__main__':
    s = Solution()
    A = ["cba", "daf", "ghi"]
    r = s.minDeletionSize(A)
    print(r)
    A = ["zyx", "wvu", "tsr"]
    r = s.minDeletionSize(A)
    print(r)
