class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}

        def helper(i, m, n):
            if i == len(strs):
                return 0
            elif (i, m, n) in memo:
                return memo[(i, m, n)]

            c0, c1 = strs[i].count('0'), strs[i].count('1')
            if m < c0 or n < c1:
                r = helper(i + 1, m, n)
            else:
                r = max(helper(i + 1, m, n),
                        1 + helper(i + 1, m - c0, n - c1))
            memo[(i, m, n)] = r
            return r
        return helper(0, m, n)


if __name__ == '__main__':
    s = Solution()
    strs = [
        '10', '0001', '111001', '1', '0'
    ]
    print(strs)
    r = s.findMaxForm(strs, 5, 3)
    print(r)

    strs = ["10", "0", "1"]
    r = s.findMaxForm(strs, 1, 1)
    print(r)

    strs = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101",
            "0", "11", "01", "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
    r = s.findMaxForm(strs, 9, 80)
    print(r)
