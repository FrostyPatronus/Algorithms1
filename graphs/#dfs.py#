topologicalList = None
orderCounter = None

def depthFirstSearch(graph, start):
    explored = []
    isTopologicalOrder = orderCounter != None

    def dfs(node):
        global topologicalList
        global orderCounter
    
        explored.append(node)
        for connectedNode in graph[node]:
            if connectedNode not in explored:
                if connectedNode not in topologicalList:
                    dfs(connectedNode)

        if isTopologicalOrder:
            topologicalList[orderCounter - 1] = node
            orderCounter -= 1
        
    dfs(start)
    return explored

def topologicalOrder(graph):
    global topologicalList
    global orderCounter
    
    orderCounter = len(graph)
    topologicalList = [None] * orderCounter

    for node in graph.keys():
        if node not in topologicalList:
            depthFirstSearch(graph, node)
        
    return topologicalList
            
