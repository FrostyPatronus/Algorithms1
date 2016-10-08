# SAMPLE NODES DATA:
# [Node1, Node2] where Node* is a string

# SAMPLE EDGES DATA:
# [(Node1, Node2), (Node3, Node4)]
from contract import contract

adjList = {}

# Populates the adjacency list
def populateAdjList(raw):
    raw = raw.splitlines()

    for line in raw:
        temp = line.split("\t")

        key = temp[0]
        value = temp[1 : ]

        adjList[key] = value

def main():
    global adjList

    # Populates the adjacency list
    raw = open("adjacencyList.txt", "r").read()
    populateAdjList(raw)

    print adjList

    contract(adjList)
    print adjList

    contract(adjList)
    print adjList

if __name__ == "__main__":
    main()