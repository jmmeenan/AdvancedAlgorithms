def subset_sum(nums: list[int], sum: int) -> bool:
    n = len(nums)
    
    matrix = [[False for j in range(sum+1)] for i in range(n+1)]
    
    #printMatrix(matrix)
    for i in range(n+1):
        matrix[i][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if nums[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-nums[i-1]]
    #printMatrix(matrix)
    return matrix[n][sum]


def min_trials(n, k)-> int:
    matrix = [[0 for j in range(k+1)] for i in range(n+1)]

    for i in range(1, n+1):
        matrix[i][1] = 1

    for j in range(1, k+1):
        matrix[1][j] = j

    for i in range(2, n+1):
        for j in range(2, k+1):
            matrix[i][j] = float('inf')
            for x in range(1, j+1):
                matrix[i][j] = min(matrix[i][j], 1 + max(matrix[i-1][x-1], matrix[i][j-x]))
    #printMatrix(matrix)
    return matrix[n][k]

def split_rope(prices, n):
    matrix = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            matrix[i] = max(matrix[i], prices[j-1] + matrix[i-j])
    #print(matrix)
    return matrix[n]


def sumCount(m,n,x):
    
    matrix = [[0] * (x+1) for i in range(n+1)]
    matrix[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, x+1):
            for k in range(1, min(j, m)+1):
                matrix[i][j] += matrix[i-1][j-k]
    return matrix[n][x]

def printMatrix(x):
    for i in x:
        print(i)


    




def num_combinations(code, M):
    MOD = 10**9 + 7
    n = len(code)
    matrix = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(0,n):
        if int(code[i:n])<=M and int(code[i:n]) >= 1 and code[i] != '0':
            matrix[0][i] = 1
            #print(int(code[i:n]))
            #printMatrix(matrix)
        
    
    for i in range(1,n):
        row = 0
        for k in range(0,n):
            row += matrix[k][n-i]
        for j in range(0, n-i):
            if int(code[j:n-i])<=M and int(code[j:n-i]) >= 1 and code[j] != '0': #Took me an hour to figure out my problem was I put <M not <=M :p
                matrix[i][j] += row
                if j == 0:
                    matrix[i][j] +=  matrix[i-1][j]
                #print(int(code[j:n-i]))
                #printMatrix(matrix)

    return matrix[n-1][0]


if __name__ == "__main__":
    print("Tests for sums")
    print(subset_sum([1,2,4,8], 11))
    print(subset_sum([1,2,4,8], 16))

    print("Min Trials Test cases")
    print(min_trials(2,10))
    print(min_trials(2,100))

    print("Slit rope test cases")
    print(split_rope([1,5,6,9], 4))
    print(split_rope([8], 1))

    print("Sum count Tests")
    print(sumCount(2,2,3))

    print("Combinations tests")
    print(num_combinations("1234", 1000))#7
    print(num_combinations("1234", 10000))#8
    print(num_combinations("2131", 31))#5
    print(num_combinations("1200", 50))#5
    print(num_combinations("89817", 10000))#15
    print(num_combinations("3241231231322412314", 50))#6765
    print(num_combinations("787812731231231241212141535353121312315", 100))#102334155

