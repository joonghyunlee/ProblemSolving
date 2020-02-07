class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        memo = {}
        choice = [False] * (maxChoosableInteger + 1)

        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        def hash(choice):
            num = 0
            for i in range(1, maxChoosableInteger + 1):
                if choice[i]:
                    num |= (1 << i)
            return num

        def helper(desiredTotal):
            if desiredTotal <= 0:
                return False

            key = hash(choice)

            if key in memo:
                return memo[key]

            for i in range(1, maxChoosableInteger + 1):
                if not choice[i]:
                    choice[i] = True
                    if not helper(desiredTotal - i):
                        memo[key] = True
                        choice[i] = False
                        return True
                    choice[i] = False
                
            memo[key] = False

            return memo[key]

        return helper(desiredTotal)


if __name__ == '__main__':
    s = Solution()
    print s.canIWin(10, 11)
    print s.canIWin(10, 40)
        