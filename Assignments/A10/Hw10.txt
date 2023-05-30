import heapq

def removeStones(stones: list[list[int]]) -> int:
    n = len(stones)
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                graph[i].append(j)
                graph[j].append(i)
    visited = set()
    count = 0
    for i in range(n):
        if i not in visited:
            stack = [i]
            visited.add(i)
            while stack:
                node = stack.pop()
                count += 1
                for neighbors in graph[node]:
                    if neighbors not in visited:
                        visited.add(neighbors)
                        stack.append(neighbors)
            count -= 1
    return count

def no_of_islands(map_grid):
    if not map_grid:
        return 0
    m, n = len(map_grid), len(map_grid[0])
    visited = [[False for j in range(n)] for i in range(m)]
    #print(visited)
    count = 0
    for i in range(m):
        #printMatrix(visited)
        for j in range(n):
            if map_grid[i][j] == "1" and not visited[i][j]:
                dfs(map_grid, visited, i, j)
                count += 1
    return count

def printMatrix(graph):
    for i in graph:
        print(i)
    print()

def dfs(map_grid, visited, i, j):
    m, n = len(map_grid), len(map_grid[0])
    #i, j out of range, i,j on map is 0, or i,j is in visted just return
    if i < 0 or i >= m or j < 0 or j >= n or map_grid[i][j] == "0" or visited[i][j]:
        return
    visited[i][j] = True
    dfs(map_grid, visited, i+1, j)
    dfs(map_grid, visited, i-1, j)
    dfs(map_grid, visited, i, j+1)
    dfs(map_grid, visited, i, j-1)
    #printMatrix(visited)

def cheapest_flight(n, tickets, start):
    allCosts = [float('inf')] * n
    allCosts[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        curCost, curAirport = heapq.heappop(heap)
        
        if curCost > allCosts[curAirport]:
            continue
        
        for neighbor, cost in enumerate(tickets[curAirport]):
            if cost == 0:
                continue
            newCost = curCost + cost
            if newCost < allCosts[neighbor]:
                allCosts[neighbor] = newCost
                heapq.heappush(heap, (newCost, neighbor))
    
    return allCosts

def number_of_moves(start_config, end_config, forbidden_configs):
    forbidden_set = set(forbidden_configs)
    queue = [(start_config, 0)]
    visited = set()
    
    while queue:
        config, distance = queue.pop(0)
        
        if config == end_config:
            return distance
        if config in forbidden_set or config in visited:
            continue
        
        visited.add(config)
        next_configs = []

        for i in range(4):
            digit = int(config[i])
            next_configs.append(config[:i] + str((digit + 1) % 10) + config[i + 1:])
            next_configs.append(config[:i] + str((digit - 1) % 10) + config[i + 1:])
    
        for next_config in next_configs:
            if next_config not in forbidden_set and next_config not in visited:
                queue.append((next_config, distance + 1))
    
    return -1


def word_games(word1, word2, dictionary):
    d = set(dictionary)
    
    
    if word2 not in d:
        return -1
    
    
    queue = [(word1, 0)]
    
    
    visited = set([word1])
    
    
    while queue:
        cur, curD = queue.pop(0)
        
        if cur == word2:
            return curD
        
        for i in range(len(cur)):
            for j in range(26):
                new_word = cur[:i] + chr(ord('a') + j) + cur[i+1:]
                
                if new_word in d and new_word not in visited:
                    queue.append((new_word, curD + 1))
                    visited.add(new_word)
    
    return -1




if __name__ == "__main__":
    print("Q1 Test")
    print(removeStones([[0,0], [0,1], [1,0], [1,2], [2,1], [2,2]]))
    print(removeStones([[0,0]]))
    print("Q2 Test")
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print(no_of_islands(grid))
    print("Q3 Test")
    n = 3
    start = 0
    tickets = [[0,50,40],[20,0,10],[60,5,0]]
    print(cheapest_flight(n, tickets, start))
    print("Q4 Test")
    start_config = '9999'
    end_config = '0000'
    forbidden_configs = ['5189' ,'5123']
    print(number_of_moves(start_config, end_config, forbidden_configs))
    forbidden_configs = ['0000', '1111']
    print(number_of_moves(start_config, end_config, forbidden_configs))
    print("Q5 Test")
    word1 = "aa"
    word2 = "ac"
    dictionary = ["aa", "bb", "ac"]
    print(word_games(word1, word2, dictionary))
    word1 = "aa"
    word2 = "bb"
    dictionary =["aa", "ab", "bb"]
    print(word_games(word1, word2, dictionary))