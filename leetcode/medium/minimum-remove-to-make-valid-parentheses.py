class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                res.append('')
                stack.append((c, i))
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    lp, lpi = stack.pop()
                    res[lpi] = lp
                    res.append(c)
                else:
                    res.append('')
            else:
                res.append(c)

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    r = s.minRemoveToMakeValid('lee(t(c)o)de)')
    print(r)
    r = s.minRemoveToMakeValid('a)b(c)d')
    print(r)
    r = s.minRemoveToMakeValid('))((')
    print(r)
    r = s.minRemoveToMakeValid('(a(b(c)d)')
    print(r)