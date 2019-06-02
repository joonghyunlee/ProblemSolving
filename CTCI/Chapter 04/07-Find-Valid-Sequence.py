class GraphNode(object):
    def __init__(self, x):
        self.val = x
        self.selected = False
        self.precedings = 0
        self.next = []

    def connect(self, node):
        self.next.append(node)


def findValidSequence(projects, dependencies):
    nodes, nmap = [], {}
    for project in projects:
        node = GraphNode(project)
        nodes.append(node)
        nmap[project] = node

    for dep in dependencies:
        f, s = dep
        fnode, snode = nmap[f], nmap[s]
        fnode.connect(snode)
        snode.precedings += 1

    seq = []
    while len(seq) < len(nodes):
        nx = None
        for n in nodes:
            if not n.selected and n.precedings == 0:
                nx = n
                nx.selected = True
                break

        if not nx:
            return None

        seq.append(nx.val)
        for nn in nx.next:
            nn.precedings -= 1

    return seq


class StateGraphNode(object):
    def __init__(self, x):
        self.val = x
        self.inDFSTraversal = False
        self.selected = False
        self.next = []

    def connect(self, node):
        self.next.append(node)


def findValidSequenceByDFS(projects, dependencies):
    def dfs(node, seq):
        if node.selected:
            return True
        if node.inDFSTraversal:
            return False

        node.inDFSTraversal = True
        for nx in node.next:
            if dfs(nx, seq) is False:
                return False
        node.selected = True
        seq.insert(0, node.val)
        return True

    nodes, nmap = [], {}
    for project in projects:
        node = StateGraphNode(project)
        nodes.append(node)
        nmap[project] = node

    for dep in dependencies:
        f, s = dep
        fnode, snode = nmap[f], nmap[s]
        fnode.connect(snode)

    seq = []
    for node in nodes:
        if dfs(node, seq) is False:
            return None
    return seq


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [
        ('a', 'd'),
        ('f', 'b'),
        ('b', 'd'),
        ('f', 'a'),
        ('d', 'c')
    ]
    r = findValidSequence(projects, dependencies)
    print r

    r = findValidSequenceByDFS(projects, dependencies)
    print r
