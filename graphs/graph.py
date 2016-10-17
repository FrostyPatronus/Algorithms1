import contract as c
import bfs
import connectivity as con

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

    print con.connectivity(adjList)


if __name__ == "__main__":
    # Populates the adjacency list
    raw = open("adjacencyList.txt", "r").read()
    populateAdjList(raw)

    main()
