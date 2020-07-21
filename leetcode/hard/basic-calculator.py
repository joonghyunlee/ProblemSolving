class Solution:
    def calculate(self, s: str) -> int:
        s = '(' + s.replace(' ', '') + ')'
        postfix = []
        operators = []
        num = None
        for c in s:
            if c in '0123456789':
                num = 0 if num is None else num * 10
                num += (ord(c) - ord('0'))
            else:
                if num is not None:
                    postfix.append(num)
                    num = None
                if c == '(':
                    operators.append(c)
                elif c == ')':
                    while operators and operators[-1] != '(':
                        postfix.append(operators.pop())
                    operators.pop()
                else:
                    while operators and operators[-1] != '(':
                        postfix.append(operators.pop())
                    operators.append(c)

        while operators:
            postfix.append(operators.pop())

        value = []
        for e in postfix:
            if type(e) == int:
                value.append(e)
            elif e == '+':
                a = value.pop()
                b = value.pop()
                value.append(a + b)
            elif e == '-':
                a = value.pop()
                b = value.pop()
                value.append(b - a)
            
        return value.pop()


if __name__ == '__main__':
    s = Solution()
    r = s.calculate("1 + 1")
    print(r)
    r = s.calculate("2-1 + 2")
    print(r)
    r = s.calculate("(1+(4+5+2)-3)+(6+8)")
    print(r)
    r = s.calculate(" 100 + 1")
    print(r)
