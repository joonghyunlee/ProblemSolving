class Solution:
    def numIdenticalPairs(self, nums: 'List[int]') -> int:
        def combination(n: int) -> int:
            return n * (n - 1) // 2

        from collections import Counter
        cnt = Counter(nums)

        answer = 0
        for value in cnt.values():
            if value > 1:
                answer += combination(value)
        return answer


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    r = s.numIdenticalPairs(nums)
    print(r)
    nums = [1, 1, 1, 1]
    r = s.numIdenticalPairs(nums)
    print(r)
    nums = [1, 2, 3]
    r = s.numIdenticalPairs(nums)
    print(r)
