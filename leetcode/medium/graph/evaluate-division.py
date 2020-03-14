class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        eqs = collections.defaultdict(dict)
        for equation, value in zip(equations, values):
            dividend, divisor = equation
            eqs[dividend][divisor] = value
            eqs[divisor][dividend] = 1.0 / value
        
        def dfs(a, b):
            stack = [(a, 1.0)]
            visit = {a}
            while stack:
                dividend, value = stack.pop()
                if dividend == b:
                    return value
                for divisor in eqs[dividend].keys():
                    if divisor not in visit:
                        visit.add(divisor)
                        stack.append((divisor, eqs[dividend][divisor] * value))
            return -1.0

        ans = []
        for query in queries:
            dividend, divisor = query
            if dividend not in eqs.keys() or divisor not in eqs.keys():
                ans.append(-1.0)
            else:
                ans.append(dfs(dividend, divisor))

        return ans


if __name__ == '__main__':
    s = Solution()
    equations = [['a', 'b'], ['b', 'c']]
    values = [2.0, 3.0]
    queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]
    r = s.calcEquation(equations, values, queries)
    print(r)