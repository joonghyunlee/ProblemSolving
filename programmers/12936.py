def solution(n, k):
    answer = []
    factorial = [1]
    for i in range(1, n):
        factorial.append(i * factorial[i - 1])

    def helper(nums, i, k):
        if k == 0:
            for num in nums:
                answer.append(num)
            return
        digit = k // factorial[i]
        k %= factorial[i]
        answer.append(nums[digit])
        helper(nums[:digit] + nums[digit + 1:], i - 1, k)
    
    helper(list(range(1, n + 1)), n - 1, k - 1)
    return answer

if __name__ == '__main__':
    r = solution(4, 10)
    print r
    r = solution(5, 32)
    print r