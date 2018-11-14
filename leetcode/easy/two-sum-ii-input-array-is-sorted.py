class Solution(object):
    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                s = numbers[i] + numbers[j]
                if s == target:
                    return [i + 1, j + 1]
                elif s > target:
                    break

    def twoSum(self, numbers, target):
        def m(x, y):
            return numbers[x] + numbers[y]

        a = 0
        b = len(numbers) - 1
        while a < b:
            if m(a, b) == target:
                return [a + 1, b + 1]
            elif m(a, b) > target:
                b -= 1
            else:
                a += 1


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2, 7, 11, 15], 9)
    print r
    s = Solution()
    r = s.twoSum([2, 3, 4], 6)
    print r


    import random
    for _ in range(10):
        numbers = sorted(random.sample(xrange(1, 101), 20))
        a = random.choice(numbers)
        b = random.choice(numbers)
        target = a + b
        print "nums: "
        print numbers
        diff = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
        print "a(%d) + b(%d) = target(%d)" % (a, b, target)
        r = s.twoSum(numbers, target)
        print r
