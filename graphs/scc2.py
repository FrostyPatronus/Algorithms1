import heapq
import sys

import resource

sys.setrecursionlimit(10**6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

class scc:
    def __init__(self, graph):
        self.graph = graph
        
        self.explored = set()
        self.finishingTimes = {}

        self.progress = 0

        self.main()

    def main(self):

        # Call DFS loop on transposed graph

        print "In main"
        self.firstPass(self.transposedGraph())
        print "done with first pass"
        results = self.secondPass(self.graph)

        # print results
        print heapq.nlargest(5, map(len, results))
        
        print "done with sec pass"
        
        
    def firstPass(self, graph):
        for key in graph:
            if key not in self.explored:
                self.dfs1(graph, key)
                
        # print self.finishingTimes
    
    def dfs1(self, graph, source):
        self.explored.add(source)
        
        for edge in graph[source]:
            if edge not in self.explored:
                self.dfs1(graph, edge)
                
        self.progress += 1
        self.finishingTimes[self.progress] = source

    # Collects all the SCC lengths
    def secondPass(self, graph):
        self.explored = set()

        # sccLengths = set()
        sccs = []

        progress = len(graph)

        while progress > 0:
            node = self.finishingTimes[progress]

            if node not in self.explored:
                subGraph = self.dfs2(graph, node)
            
                print node, progress
                # print node
                
                sccs.append(subGraph)
                
            progress -= 1
            
        return sccs
    
    def dfs2(self, graph, key):
        localExplored = []
        
        def recursion(node):
            self.explored.add(node)
            localExplored.append(node)
            
            for edge in graph[node]:
                if edge not in self.explored:
                    recursion(edge)

        recursion(key)

        return localExplored
        
    # Returns a transposed graph from self.graph
    def transposedGraph(self):
        sourceGraph = self.graph

        revGraph = {}
        
        for node, edges in sourceGraph.iteritems():

            # Ensures all the nodes have an entry in the reversed graph
            if node not in revGraph:
                revGraph[node] = []
            
            for edge in edges:
                if edge in revGraph:
                    revGraph[edge].append(node)
                else:
                    revGraph[edge] = [node]

        return revGraph
                
