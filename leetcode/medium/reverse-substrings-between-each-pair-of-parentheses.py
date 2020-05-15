class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = [c for c in s]
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                l = stack.pop()
                r = i
                answer[l + 1:r] = reversed(answer[l + 1:r])
        return ''.join([c for c in answer if c not in ('(', ')')])


if __name__ == '__main__':
    s = Solution()
    r = s.reverseParentheses('(abcd)')
    print(r)
    r = s.reverseParentheses('(u(love)i)')
    print(r)
    r = s.reverseParentheses('(ed(et(oc))el)')
    print(r)