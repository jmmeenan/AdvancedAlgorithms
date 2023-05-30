class Graph:
    def __init__(self, n, edges):
        self.size = n
        self.map = {}
        for start, end in edges:
            if start in self.map.keys():
                self.map[start].append(end)
            else:
                self.map[start] = [end]
        

    def route(self, src, dst):
        if src in self.map.keys():
            path = []
            possiblePaths = []
            visited = []
            for i in self.map[src]:
                possiblePaths.append((src, i))
            while possiblePaths:
                curNode = possiblePaths.pop()
                path.append(curNode)
                visited.append(curNode)
                if curNode[1] == dst:
                    return path
                else:
                    newPaths = []
                    if curNode[1] in self.map.keys():
                        for i in self.map[curNode[1]]:
                            if (curNode[1], i) not in visited:
                                newPaths.append((curNode[1], i))
                        if len(newPaths) == 0:
                            path.pop()
                        else:
                            possiblePaths.extend(newPaths)
                    else:
                        path.pop()
        
        return []
        

if __name__ == "__main__":
    arr =  [(0, 1), (1, 2), (0, 2), (2, 3)]
    
    g1 = Graph(3, arr)
    print(g1.route(0,3))