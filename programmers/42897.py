def solution(money):
    def helper(nums):
        now = prev = 0
        for num in nums:
            now, prev = max(now, prev + num), now
        return now

    return max(helper(money[1:]), helper(money[:-1]))


if __name__ == '__main__':
    money = [1, 2, 3, 1]
    print solution(money)
    money = [1, 2, 3, 4, 5]
    print solution(money)
    money = [4, 2, 3, 8, 5]
    print solution(money)