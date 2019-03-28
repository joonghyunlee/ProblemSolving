class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for token in tokens:
            if token == '+':
                s.append(s.pop() + s.pop())
            elif token == '-':
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif token == '*':
                s.append(s.pop() * s.pop())
            elif token == '/':
                a, b = s.pop(), s.pop()
                s.append(int(float(b) / float(a)))
            else:
                s.append(int(token))
        return s[0] if s else 0


if __name__ == '__main__':
    s = Solution()
    r = s.evalRPN(['2', '1', '+', '3', '*'])
    print r
    r = s.evalRPN(['4', '13', '5', '/', '+'])
    print r
    r = s.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
    print r
    r = s.evalRPN(['4', '3', '-'])
    print r
