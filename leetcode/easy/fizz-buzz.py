class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        seq = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                item = 'FizzBuzz'
            elif i % 5 == 0:
                item = 'Buzz'
            elif i % 3 == 0:
                item = 'Fizz'
            else:
                item = str(i)
            seq.append(item)
        return seq


if __name__ == '__main__':
    s = Solution()
    r = s.fizzBuzz(15)
    print(r)
