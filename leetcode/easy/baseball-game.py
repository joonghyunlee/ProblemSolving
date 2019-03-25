class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        s = []
        for op in ops:
            if op == '+':
                s.append(s[-1] + s[-2])
            elif op == 'D':
                s.append(s[-1] * 2)
            elif op == 'C':
                s.pop()
            else:
                s.append(int(op))
        return sum(s)


if __name__ == '__main__':
    s = Solution()
    r = s.calPoints(['5', '2', 'C', 'D', '+'])
    print r
    r = s.calPoints(["5","-2","4","C","D","9","+","+"])
    print r
