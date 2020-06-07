from itertools import combinations

def solution(relation):
    nr = len(relation)
    nc = len(relation[0]) if relation else 0
    uniques = []
    for i in range(1, nc + 1):
        combs = combinations(range(nc), i)
        for candidate in list(combs):
            items = set()
            for record in relation:
                items.add(tuple(record[col] for col in candidate))
            if len(items) == nr:
                uniques.append(set(candidate))

    keys = []
    for unique in uniques:
        if len(unique) == 1:
            keys.append(unique)
        if all(key & unique != key for key in keys):
            keys.append(unique)

    return len(keys)


if __name__ == '__main__':
    relation = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]
    r = solution(relation)
    print(r)