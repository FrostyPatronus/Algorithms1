import sys
import resource
import heapq

sys.setrecursionlimit(2**20)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

from copy import deepcopy

explored = {}
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
        explored[node] = None
        # print "[EXPLORED]:",  explored
    
        for vertex in adjList[node]:
            if vertex not in explored:
                recursion(adjList, vertex)

        time += 1

        # [Finishing Time] : [Node]
        finishingTime[time] = node

    recursion(adjList, node)
    return connection

def dfsLoop(adjList):
    vertices = [int(i) for i in adjList.keys()]
    connected = []

    # [str(i) for i in range(getMaxNode(adjList), 0, -1)]:
    for node in adjList:
        if node not in explored:
            connection = dfs(adjList, node)
            # print connection
            connected.append(connection)
                        
    return connected

def reverseGraph(adjList):
    graph = deepcopy(adjList)

    # Initialize reversed graph
    reversedGraph = {key: [] for key in graph}

    for node, edges in graph.iteritems():
        for adjacent in edges:
            reversedGraph[adjacent].append(node)

    return reversedGraph

def findSCC(adjList):
    global explored
    
    explored = {}
    graph = reverseGraph(adjList)

    connectedComponents = []

    localTime = time

    while localTime != 0:
        component = dfs(graph, finishingTime[localTime])
        localTime -= len(component)
        connectedComponents.append(component)
    return connectedComponents
    # return connectedComponents

def scc(adjList):
    # print "LIST:", adjList
    print "DFS LOOP"
    dfsLoop(adjList)
    # print finishingTime
    # print adjList
    # print reverseGraph(adjList)
    
    results = findSCC(adjList) 

    # print heapq.nlargest(5, [len(i) for i in results])
    print results
