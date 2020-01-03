def solution(participant, completion):
    completion_map = {}
    for comp in completion:
        completion_map[comp] = completion_map.get(comp, 0) + 1

    uncompletions = []
    for part in participant:
        v = completion_map.get(part, 0)
        if v <= 0:
            uncompletions.append(part)
        else:
            completion_map[part] = v - 1

    return uncompletions[0] if uncompletions else ''


if __name__ == '__main__':
    participant = ['leo', 'kiki', 'eden']
    completion = ['eden', 'kiki']
    r = solution(participant, completion)
    print r
    participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    completion = ['josipa', 'filipa', 'marina', 'nikola']
    r = solution(participant, completion)
    print r
    participant = ['mislav', 'stanko', 'mislav', 'ana']
    completion = ['stanko', 'ana', 'mislav']
    r = solution(participant, completion)
    print r
    participant = ['leo']
    completion = []
    r = solution(participant, completion)
    print r