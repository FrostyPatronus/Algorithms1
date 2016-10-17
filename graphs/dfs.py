def depthFirstSearch(graph, start):
    explored = []

    def dfs(node):
        explored.append(node)
        for connectedNode in graph[node]:
            if connectedNode not in explored:
                dfs(connectedNode)

    dfs(start)
    return explored
