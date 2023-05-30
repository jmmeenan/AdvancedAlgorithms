def merge_sort(l: list[int]) -> list[int]:
    output = []
    length = len(l)
    if length == 0:
        return output
    if length > 1:
        m = length // 2
        L = merge_sort(l[0:m])
        R = merge_sort(l[m:])
        return merge(L, R)

    return l

def merge(L: list[int], R: list[int]) -> list[int]:
    output = []
    countL = 0
    countR = 0
    if len(L) == 1 and len(R) == 1:
        if R[0] < L[0]:
            return [R[0], L[0]]
        else:
            return [L[0], R[0]]
    while countL < len(L):
        while countR < len(R):
            if countL == len(L):
                output.append(R[countR])
                countR += 1
            elif R[countR] > L[countL]:
                output.append(L[countL])
                countL += 1
            elif R[countR] <= L[countL]:
                output.append(R[countR])
                countR += 1
        if countL != len(L):
            output.append(L[countL])
            countL += 1
        
    return output


if __name__ == '__main__':
    print(merge_sort([4,1,3,2]))
    l = []
    for i in range(100, 0, -1):
        l.append(i)
    print(l)
    print(merge_sort(l))
    print(merge_sort([1,2,3,4]))