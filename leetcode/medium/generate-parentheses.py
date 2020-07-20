class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        res = []

        def helper(prev, lp, rp):
            if lp == 0 and rp == 0:
                res.append(prev)
            elif lp < 0 or rp < 0:
                return

            if lp == rp:
                helper(prev + '(', lp - 1, rp)
            else:
                helper(prev + '(', lp - 1, rp)
                helper(prev + ')', lp, rp - 1)
        helper('(', n - 1, n)
        return res
