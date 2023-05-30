def binaryString(allElem, n, l, curLength):
    if n == curLength:
        allElem.append(l)
        return [l]
    if l[curLength-1] == '0':
        hold = l
        hold += '0'
        i = []
        i += [binaryString(allElem, n,hold,curLength+1)]
        l += '1'
        i += [binaryString(allElem, n,l,curLength+1)]
        return i

    if l[curLength-1] == '1':
        l += '0'
        return binaryString(allElem, n, l, curLength+1)
    pass

def pattern(n: int) -> list[str]:
    if n <= 0:
        return []
    output = []
    l = '0'
    binaryString(output, n, l, 1)
    #for i in binaryString(n, l, 1):
        #output.append(i)

    l = '1'
    binaryString(output, n, l, 1)
    #for i in binaryString(n, l, 1):
        #output.append(i)

    return output


if __name__ == '__main__':
    print(pattern(1))
    