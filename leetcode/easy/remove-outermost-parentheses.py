class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        answer = ''
        for i, c in enumerate(S):
            if c == '(':
                stack.append((i, c))
            elif c == ')':
                if stack and stack[0][1] == '(':
                    pi, _ = stack.pop()
                    if len(stack) == 0:
                        answer += S[pi + 1:i]
        return answer

    def removeOuterParentheses2(self, S: str) -> str:
        l, r = 0, 0
        inner = ''
        for i, c in enumerate(S):
            if c == '(':
                l += 1
            elif c == ')':
                r += 1
            if l > 0 and r > 0 and l == r:
                inner += S[i - (l + r) + 2:i]
                l = r = 0
        return inner


if __name__ == '__main__':
    s = Solution()
    r = s.removeOuterParentheses('(()())(())')
    print(r)
    r = s.removeOuterParentheses2('(()())(())')
    print(r)
    r = s.removeOuterParentheses('(()())(())(()(()))')
    print(r)
    r = s.removeOuterParentheses2('(()())(())(()(()))')
    print(r)

