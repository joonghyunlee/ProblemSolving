def solution(food_times, k):
    foods = [(i + 1, f) for i, f in enumerate(food_times)]
    foods.sort(key=lambda x: x[1])
    n = len(food_times)
    prev = 0
    for i in range(n):
        time = foods[i][1]
        if time == prev:
            continue
        if k < (time - prev) * (n - i):
            return sorted(foods[i:], key=lambda x: x[0])[k % (n - i)][0]
        k -= (time - prev) * (n - i)
        prev = time
    return -1


if __name__ == '__main__':
    food_times = [3, 1, 2]
    r = solution(food_times, 5)
    print(r)
    food_times = [3, 1, 1, 1, 2, 4, 3]
    r = solution(food_times, 12)
    print(r)