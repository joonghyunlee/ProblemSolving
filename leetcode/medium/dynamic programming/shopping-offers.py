class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = {}
        def helper(items):
            if sum(items) == 0:
                return 0
            if tuple(items) in memo:
                return memo[tuple(items)]
            pay = sum(map(lambda x, y: x * y, items, price))
            for offer in special:
                nextItems = list(map(lambda x, y: x - y, items, offer[:-1]))
                if all(map(lambda x: x >= 0, nextItems)):
                    pay = min(pay, offer[-1] + helper(nextItems))
            memo[tuple(items)] = pay
            return pay
        return helper(needs)


if __name__ == '__main__':
    s = Solution()
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    r = s.shoppingOffers(price, special, needs)
    print r

    price = [2, 3, 4]
    special = [[1, 1, 0, 4], [2, 2, 1, 9]]
    needs = [1, 2, 1]
    r = s.shoppingOffers(price, special, needs)
    print r
            
