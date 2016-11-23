import contract as c
import bfs
import connectivity as con
import dfs
import scc
import sys
import dijkstra
import scc2

adjList = {}

def populateAdjListWeighted(raw):
    raw = raw.splitlines()
    
    for line in raw:
        temp = line.strip().split("\t")

        key = temp[0]
        raw_values = temp[1: ]
        
        values = []
        
        for value in raw_values:
            pair = value.split(",")
            pair[1] = int(pair[1])
            values.append((pair[0], pair[1]))
        
        adjList[key] = values

    # print adjList

# Populates the adjacency list
def populateAdjList(raw):
    global adjList
    raw = raw.splitlines()

    for line in raw:
        if not line:
            continue
        
        temp = [int(i) for i in line.strip().split(" ")]

        key = temp[0]
        value = temp[1:]

        if adjList.has_key(key):
            adjList[key].extend(value)
        else:
            adjList[key] = value


        for edge in value:
            if not adjList.has_key(edge):
                adjList[edge] = []
        
        # adjList[key] = value

    print "Finished creating Adj List"
    # print adjList


    
def main():
    global adjList
    
    # Outputs the strongly connected components of a graph
    scc2.scc(adjList)
    

if __name__ == "__main__":
    # Populates the adjacency list
    raw = open("scc.txt", "r").read()
    # adjList = {key: [] for key in range(1, 875714 + 1)}
    
    # print adjList
    # populateAdjListWeighted(raw)

    populateAdjList(raw)
    # print adjList

    main()
    
