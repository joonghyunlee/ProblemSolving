class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        targets = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            targets[src].append(dst)
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]


if __name__ == '__main__':
    s = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    r = s.findItinerary(tickets)
    print(r)
    tickets = [["JFK", "SFO"], ["JFK", "ATL"],
               ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    r = s.findItinerary(tickets)
    print(r)
    tickets = [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], 
               ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"],
               ["ANU", "TIA"], ["JFK", "TIA"]]
    r = s.findItinerary(tickets)
    print(r)
