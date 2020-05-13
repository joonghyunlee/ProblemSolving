def solution(p):
    def split(text):
        if len(text) < 2:
            return text, ''
        i, l, r = 0, 0, 0
        for i, c in enumerate(text):
            if c == '(':
                l += 1
            elif c == ')':
                r += 1
            if l > 0 and r > 0 and l == r:
                break
        return text[:i + 1], text[i + 1:]

    def correct(text):
        stack = []
        for c in text:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0

    def reverse(text):
        rev = []
        for c in text:
            if c == '(':
                rev.append(')')
            elif c == ')':
                rev.append('(')
        return ''.join(rev)

    def helper(text):
        if not text:
            return text
        u, v = split(text)
        if correct(u):
            answer = u + helper(v)
        else:
            answer = '('
            answer += helper(v)
            answer += ')'
            answer += ''.join(reverse(u[1:-1]))
        return answer
    
    return helper(p)


if __name__ == '__main__':
    r = solution('(()))(')
    print(r)