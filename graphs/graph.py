import contract as c
import bfs
import connectivity as con
import dfs
import scc

adjList = {}

# Populates the adjacency list
def populateAdjList(raw):
    raw = raw.splitlines()

    for line in raw:
        temp = line.strip().split(" ")

        key = temp[0]
        value = temp[1 : ]

        adjList[key] = value

def main():
    global adjList
    
    # Outputs the strongly connected components of a graph
    scc.scc(adjList)


if __name__ == "__main__":
    # Populates the adjacency list
    raw = open("adjacencyList.txt", "r").read()
    populateAdjList(raw)

    main()

    
