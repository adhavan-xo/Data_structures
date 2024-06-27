class graph:
    def __init__(self,edges,n):
        self.adjList = [[] for _ in range(n)]
        for (src,dec) in (edges) :
            self.adjList[src].append(dec)



def printgr(graph):
    for src in range (len(graph.adjList)):
        for dest in graph.adjList[src]:
            print(f"({src} -> {dest})",end ="")
        print()

if __name__ == "__main__":
    edge = [(0,1),(1,2),(2,0),(5,4),(3,0),(2,3)]
    n = 6
    graph = graph(edge,n)
    printgr(graph)


