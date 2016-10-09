import contract as c

adjList = {}

# Populates the adjacency list
def populateAdjList(raw):
    raw = raw.splitlines()

    for line in raw:
        temp = line.strip().split("\t")

        key = temp[0]
        value = temp[1 : ]

        adjList[key] = value

def main():
    global adjList

    # Populates the adjacency list
    raw = open("min-cut.txt", "r").read()
    populateAdjList(raw)

    c.findMinCut(len(adjList.keys()), adjList)
    # print c.contract(adjList)

if __name__ == "__main__":
    main()