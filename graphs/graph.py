import contract as c
import bfs
import connectivity as con
import dfs
import scc
import sys
import dijkstra

adjList = {}

def populateAdjListWeighted(raw):
    raw = raw.splitlines()
    
    for line in raw:
        temp = line.strip().split(" ")

        key = temp[0]
        raw_values = temp[1: ]

        values = []
        
        for value in raw_values:
            pair = value.split(",")
            pair[1] = int(pair[1])
            values.append(pair)
        
        adjList[key] = values

    print adjList

# Populates the adjacency list
def populateAdjList(raw):
    global adjList
    raw = raw.splitlines()
    
    for line in raw:
        temp = [int(i) for i in line.strip().split(" ")]

        key = temp[0]
        value = temp[1]

        
        adjList[key].append(value)
        
            
        # adjList[key] = value

    print "Finished creating Adj List"
    print adjList[416780]

    
def main():
    global adjList
    
    # Outputs the strongly connected components of a graph
    # scc.scc(adjList)
    dijkstra.dijkstra(adjList, "s")

if __name__ == "__main__":
    # Populates the adjacency list
    raw = open("adjacencyList.txt", "r").read()
    # adjList = {key: [] for key in range(1, 875714 + 1)}
    
    # print adjList

    populateAdjListWeighted(raw)

    main()

    
