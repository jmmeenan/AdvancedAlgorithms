def max_loot(trees: list[int]) -> int:
    numOfElem = len(trees)
    if numOfElem == 0:
        return 0
    elif numOfElem == 1:
        return trees[0]
    else:
        nextMax = 0
        maxHold = trees[0]
        count = 1
        while count < numOfElem:
            temp = maxHold
            maxHold = max(maxHold, nextMax + trees[count])
            nextMax = temp
            count += 1
        return maxHold



if __name__ == "__main__":
    print(max_loot([5, 10, 20, 5]))
    print(max_loot([2,1,1,1,20]))
    print(max_loot([]))
    print(max_loot([10, 20]))
    print(max_loot([2,1,1,20]))
