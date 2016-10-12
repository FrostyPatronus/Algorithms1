import copy
import collections as col

def breadthFirstSearch(graph, startVertex):
    graph = copy.deepcopy(graph)
    deque = col.deque([startVertex])

    explored = {startVertex : 0}

    while deque:
        node = deque.popleft()

        for adjNode in graph[node]:
            nodesOfAdjNode = graph[adjNode]

            if adjNode not in explored.keys() and adjNode not in deque:
                deque.append(adjNode)
                explored[adjNode] = explored[node] + 1

    return explored
