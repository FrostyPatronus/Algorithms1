import heapq 

def dijkstra(graph, source):
    graphSize = len(graph)

    scores = {source: 0}
    
    while graphSize >= len(scores):

        greedySentry = None
        sourceNode = None

        # Exhaustive comparisons
        for node in scores:

            for edge in graph[node]:
                # [ 0 ] -> Outgoing node
                # [ 1 ] -> Edge weight
                
                outNode = edge[0]
                weight = edge[1]

                # Stops if the outgoing node is in explored
                if outNode in scores:
                    continue

                # Initializes in the first pass
                if greedySentry == None:
                    greedySentry = edge
                    sourceNode = node
                    continue

                greedyWeight = greedySentry[1]

                # Replaces counter if weight is less
                if greedyWeight > weight:
                    greedySentry = edge
                    sourceNode = node

        # print greedySentry
        # print scores[sourceNode]
        
        scores[greedySentry[0]] = greedySentry[1] + scores[sourceNode]

    print scores

# Sample dict 
# {Node : [ [Edge1, weight], [Edge2, weight] ]}
    
def dijkstraHeap(graph, source):
    print graph
    heap = []

    # Iterate over nodes
    for node in graph:
        if node == source:
            heap.append((0, node))
        heap.append((float("inf"), node))
    heapq.heapify(heap)

    graphSize = len(graph)
    explored = {}
    exploredSize = 0
    
    while exploredSize < graphSize:
        exploredScore, exploredNode = heapq.heappop(heap)

        if exploredNode in explored:
            continue
        
        explored[exploredNode] = exploredScore
        
        for edge, edgeWeight in graph[exploredNode]:
            # Check if node is in the heap
            if edge not in explored:
                heapq.heappush(heap, (edgeWeight + exploredScore, edge))
                
        exploredSize += 1
        
    return explored

# Answer to the quiz is 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
