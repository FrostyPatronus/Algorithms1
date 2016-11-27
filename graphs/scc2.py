import heapq
import sys

import time

import resource

sys.setrecursionlimit(10**6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

class scc:
    def __init__(self, graph):
        self.graph = graph
        
        self.explored = set()
        self.finishingTimes = {}

        self.progress = 0
        
        t1 = time.time()

        self.main()

        t2 = time.time()
        delta = t2 - t1
        print "Time elapsed:", delta

    def main(self):

        # Call DFS loop on the graph
        
        print "In main"
        self.firstPass(self.graph)
        
        print "done with first pass"
        results = self.secondPass(self.transposedGraph())
        
        # print results
        print heapq.nlargest(5, map(len, results))
        
        print "done with sec pass"

        # Answer is [434821, 968, 459, 313, 211]
        
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
                
