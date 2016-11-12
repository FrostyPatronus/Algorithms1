def dijkstra(graph, source):
    graphSize = len(graph)

    scores = {source: 0}
    
    while graphSize >= len(scores):

        greedySentry = None
        sourceNode = None
        
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

        print greedySentry
        print scores[sourceNode]
        
        scores[greedySentry[0]] = greedySentry[1] + scores[sourceNode]

    print scores
