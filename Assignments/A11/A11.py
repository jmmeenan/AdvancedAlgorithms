def minimumCost(n: int, connections: list[list[int]]) -> int:
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
        
    connections.sort(key=lambda x: x[2])
    count = 0
    mst = []
    parent = [i for i in range(n+1)]
    
    for edge in connections:
        x, y, cost = edge
        px, py = find(parent, x), find(parent, y)
        if px != py:
            mst.append(edge)
            count += cost
            parent[px] = py
    
    return count if len(mst) == n-1 else -1

if __name__ == "__main__":
    print("Q1 Test Cases")
    print(minimumCost(3, [[1,2,4],[1,3,7],[2,3,1]]))
    print(minimumCost(4, [[1,2,3],[3,4,4]]))