from array import *

def num_subarraysHash(arr, target):
    m = {}
    total = 0
    anw = 0
    for i in arr:
        if i not in m:
            m[i] = [i]
        if i == target:
            anw += 1
        if m.__contains__(target - i):
            anw += 1
    print(m)
    return anw

def num_subarrays(arr, target):
    #cur = []
    #output = []
    total = 0
    inc = 1
    anw = 0
    if arr == []:
        return 0
    for i in arr:
        #cur = [i]
        total = i
        if total == target:
            #output.append([i])
            anw += 1
        for j in arr[inc:]:
            #cur.append(j)
            total += j
            if total == target:
                #print(cur)
                #output.insert(anw, cur)
                #output.append(cur)
                #print("Output")
                #print(output)
                anw += 1
        inc += 1
    return anw

if __name__ == '__main__':
    test1 = [5, -5, 10]
    print(num_subarrays(test1, 5))
    test2 = [1,1,0,1,1]
    print(num_subarrays(test2, 2))
    test3 = []
    print(num_subarrays(test3, 2))
    print(num_subarraysHash(test1, 5))
    test2 = [1,1,0,1,1]
    print(num_subarraysHash(test2, 2))