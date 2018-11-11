class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        if x == 0:
            return True

        if x % 10 == 0:
            return False

        y = 0
        while x > y:
            y = y * 10 + x % 10
            if x / 10 == y:
                return True
            elif x == y:
                return True
            x = x / 10

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(10))
