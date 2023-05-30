def quicksort(num : list[int]):
    lenghtOfList = len(num)
    if lenghtOfList == 0 or lenghtOfList == 1:
        return num
    left = []
    right = []
    pivot = num[lenghtOfList-1]
    for i in range(0, lenghtOfList-1):
        if num[i] > pivot:
            right.append(num[i])
        else:
            left.append(num[i])
    left = quicksort(left)
    left.append(pivot)
    right = quicksort(right)
    return left + right

if __name__ == "__main__":
    print(quicksort([5, 4, 3, 2, 1]))
    print(quicksort([3, 4, 2, 1]))
    print(quicksort([2,3,6,4,3,2,8,77,33,44,7777,888,1,2,3,4,55,55]))