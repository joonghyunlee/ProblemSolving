class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        PAREN_MAP = {
            '(': 0,
            '{': 0,
            '[': 0
        }

        PAREN_PAIR = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        open_parens = []
        for c in s:
            if c in PAREN_MAP.keys():
                PAREN_MAP[c] = PAREN_MAP[c] + 1
                open_parens.append(c)
            else:
                if len(open_parens) == 0:
                    return False

                if open_parens[-1] != PAREN_PAIR[c]:
                    return False
                else:
                    PAREN_MAP[PAREN_PAIR[c]] = PAREN_MAP[PAREN_PAIR[c]] - 1
                    open_parens.pop()

        for value in PAREN_MAP.values():
            if value != 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([)]'))
    print(s.isValid('{[]}'))
