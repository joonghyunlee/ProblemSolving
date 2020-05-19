def solution(tickets: 'List[List[str]]') -> 'List[str]':
    answer = []
    tickets.sort(key=lambda x: x[1], reverse=True)
    route = {}
    for src, dst in tickets:
        nexts = route.setdefault(src, [])
        nexts.append(dst)

    def visit(airport):
        while route.get(airport):
            visit(route[airport].pop())
        answer.append(airport)
    visit('ICN')
    return answer[::-1]


if __name__ == '__main__':
    tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
    r = solution(tickets)
    print(r)
    tickets = [['ICN', 'SFO'], ['ICN', 'ATL'],
               ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    r = solution(tickets)
    print(r)
