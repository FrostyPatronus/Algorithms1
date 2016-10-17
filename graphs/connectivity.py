import bfs

def connectivity(adjList):
    explored = []
    connected = []
    
    keys = adjList.keys()
    for key in keys:
        if key in explored:
            continue

        subgraph = bfs.breadthFirstSearch(adjList, key).keys()

        explored.extend(subgraph)
        explored.append(key)

        connected.append(subgraph)
    return connected
