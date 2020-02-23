class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    memo[i] = (memo[i - 2] if i >= 2 else 0) + 2
                elif i - memo[i - 1] > 0 and s[i - memo[i - 1] - 1] == '(':
                    memo[i] = memo[i - 1]
                    memo[i] += (memo[i - memo[i - 1] - 2]
                                if i - memo[i - 1] >= 2 else 0)
                    memo[i] += 2
                ans = max(ans, memo[i])
        return ans

    def longestValidParentheses2(self, s):
        stack = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans

    def longestValidParentheses3(self, s):
        n = len(s)
        left, right = 0, 0
        ans = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * right)
            elif right >= left:
                left, right = 0, 0

        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * right)
            elif left >= right:
                left, right = 0, 0
        return ans


if __name__ == '__main__':
    s = Solution()
    r = s.longestValidParentheses('(()')
    print r
    r = s.longestValidParentheses2('(()')
    print r
    r = s.longestValidParentheses3('(()')
    print r
    r = s.longestValidParentheses(')()())')
    print r
    r = s.longestValidParentheses2(')()())')
    print r
    r = s.longestValidParentheses3(')()())')
    print r
    r = s.longestValidParentheses('()(()')
    print r
    r = s.longestValidParentheses2('()(()')
    print r
    r = s.longestValidParentheses3('()(()')
    print r
    r = s.longestValidParentheses('()(())')
    print r
    r = s.longestValidParentheses2('()(())')
    print r
    r = s.longestValidParentheses3('()(())')
    print r
