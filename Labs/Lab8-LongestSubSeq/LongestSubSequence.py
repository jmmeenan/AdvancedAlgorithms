def lcs(s1: str, s2: str) -> int:
    matrix = []
    for i in range(len(s1)+1):
        matrix += [[0] * (len(s2)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    printMatrix(matrix)
    return matrix[len(s1)][len(s2)]

def printMatrix(matrix: list):
    for i in matrix:
        print(i)

if __name__ == "__main__":
    print("TESTS")
    s1 = "aabcdf"
    s2 = "axcfm"
    print(lcs(s1, s2))
    s1 = ""
    s2 = "abc"
    print(lcs(s1,s2))