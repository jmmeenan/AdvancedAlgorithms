def longestPalindromeSubseq(s: str) -> int:
    # your code here
    matrix = []
    length = len(s)
    
    for i in range(length):
        hold = [0]*length
        hold[i] = 1
        matrix.append(hold)

    #printMatrix(matrix)
    for i in range(2, length+1):
        for j in range(length-i+1):
            k = i + j -1
            if s[j] == s[k]:
                matrix[j][k] = 2 + matrix[j+1][k-1]
            else:
                matrix[j][k] = max(matrix[j+1][k], matrix[j][k-1])

    #printMatrix(matrix)
    return matrix[0][length-1]

def printMatrix(matrix: list):
    for i in matrix:
        print(i)

def CondensedIntegers(k, factors) -> list:
    # your code here
    output = [1]

    multiples = [0] * len(factors)

    for i in range(1, k):
        nextI = float('inf')
        for i in range(0,len(factors)):
            hold = factors[i] * output[multiples[i]]
            nextI = min(nextI, hold)

        output.append(nextI)
        for i in range(0,len(factors)):
            if nextI % factors[i] == 0:
                multiples[i] += 1

    return output





def tower_rouge(tower: list) -> int:
    if tower == []:
        return 0
    rows = len(tower)
    columns = len(tower[0])
    matrix = []
    for i in range(rows):
        hold = [0] * columns
        matrix.append(hold)
    #printMatrix(matrix)
    matrix[0][0] = tower[0][0]
    for i in range(1, rows):
        matrix[i][0] = min(matrix[i-1][0], matrix[i-1][0] + tower[i][0])
        tower[i][0] += tower[i-1][0]
    #printMatrix(matrix)
    for j in range(1, columns):
        matrix[0][j] = min(matrix[0][j-1], matrix[0][j-1] + tower[0][j])
        tower[0][j] += tower[0][j-1]
    #printMatrix(matrix)
    for i in range(1, rows):
        for j in range(1, columns):
            
            above = matrix[i-1][j]
            left = matrix[i][j-1]
            if above > left:
                matrix[i][j] = min(above, tower[i-1][j])
            else:
                matrix[i][j] = min(left, tower[i][j-1])
            
            #matrix[i][j] = min( matrix[i-1][j],matrix[i][j-1]) + tower[i][j]
    printMatrix(matrix)
   
    hold = matrix[rows-1][columns-1]
    if hold <= 0:
        return abs(hold)
    else:
        return 1



def getMedian2(arr1, arr2, n):
    # your code here
    output = 0
    if len(arr1) != len(arr2):
        return -1
    half = len(arr1)//2
    if n > 1:
        left = getMedian(arr1[0:half], arr2[0:half], len(arr2[0:half]))
        right = getMedian(arr1[half:],  arr2[half:], len(arr2[half:]))
        output = int(left) + int(right)
        output /= 2
        #print(left)
        #print(right)
    else:
        output = arr1[0] + arr2[0]
        output /= 2

    return int(output)

def getMedian(arr1, arr2, n):
    output = 0
    if len(arr1) != len(arr2):
        return -1
    allCandies = sorted(arr1 + arr2)
    return (allCandies[n-1] + allCandies[n])/2


def no_of_ways(n: int):
    # Return the number of ways 2 x 1 buildings 
    # can be arranged in 3 x n plot of land
    if n < 2:
        return 0
    Matrix = [0] * (n + 1)
    Matrix[0] = 1
    Matrix[1] = 0
    hold1 = 1
    hold2 = 0
    for i in range(2, n+1):
        Matrix[i] = Matrix[i - 2] + 2 * hold1
        hold3 = hold1
        hold1 = Matrix[i-1] + hold2
        hold2 = hold3
     
    return Matrix[n]





if __name__ == "__main__":
    print("Q1")

    print(longestPalindromeSubseq("bbab"))
    print(longestPalindromeSubseq("xyyz"))

    print()
    print("Q2")

    print(CondensedIntegers(7, [2,5,7]))
    print(CondensedIntegers(1, [2,3]))

    print()
    print("Q3")
    print(tower_rouge([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print(tower_rouge([[-5,6,0],[-9,3,10],[4,-3,-5]]))
    print(tower_rouge([[7,-1,6,7],[2,-5,-1,-8],[-1,9,2,7]]))

    print()
    print("Q4")
    print(getMedian([1,2,3,6], [4,6,8,10], 4))
    print(getMedian([1,2,3,6], [4,6,8,10,12], 4))

    print()
    print("Q5")
    #print(no_of_ways(5))
    #print(no_of_ways(4))
    print(no_of_ways(10)) #571
    #print(no_of_ways(16)) #29681
    #print(no_of_ways(18)) #110771



    