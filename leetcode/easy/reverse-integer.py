class Solution(object):
    def reverse(self, x):
        result = 0

        if x < 0:
            temp = -x
        else:
            temp = x

        while temp != 0:
            result = result * 10
            result = result + (temp % 10)
            temp = temp / 10

        if x < 0:
            result = -result

        if result > (2**31)-1:
            return 0
        elif result < -(2**31):
            return 0

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.reverse(1534236469)
    print(r)
