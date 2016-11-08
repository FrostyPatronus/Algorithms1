from copy import deepcopy

explored = []
finishingTime = {}
time = 0

def getMaxNode(adjList):
    nodes = [int(i) for i in adjList.keys()]
    return max(nodes)

def dfs(adjList, node):
    global explored
    global finishingTime
    

    connection = []
    
    def recursion(adjList, node):
        global time
        
        connection.append(node)
        explored.append(node)
        # print "[EXPLORED]:",  explored
    
        for vertex in adjList[node]:
            if vertex not in explored:
                recursion(adjList, vertex)

        time += 1
        finishingTime[node] = time

    recursion(adjList, node)
    return connection

def dfsLoop(adjList):
    vertices = [int(i) for i in adjList.keys()]
    connected = []

    for node in [str(i) for i in range(getMaxNode(adjList), 0, -1)]:
        if node not in explored:
            connection = dfs(adjList, node)
            # print connection
            connected.append(connection)
                        
    return connected

def scc(adjList):
    dfsLoop(adjList)
    print finishingTime
