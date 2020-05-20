def solution(people: 'List[int]', limit: int) -> int:
    people.sort()
    answer = 0
    l, r = 0, len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        answer += 1
    return answer


if __name__ == '__main__':
    people = [70, 50, 80, 50]
    r = solution(people, 100)
    print(r)
    people = [70, 80, 50]
    r = solution(people, 100)
    print(r)