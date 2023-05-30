def maximum_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_finish = -float('inf')
    for start, finish in intervals:
        if start >= last_finish:
            count += 1
            last_finish = finish
    return count

def circular_tour(distance, charging):
    n = len(distance)
    start = 0
    end = 0
    tank = 0
    order = 0
    while order < n:
        #print("start ", start)
        #print("distance", distance[start])
        #print("Fuel", charging[start])
        tank += charging[end] - distance[end]
        #print("tank", tank)
        #print("end", end)
        if tank < 0:
            start += 1
            end = start
            tank = 0
            order += 1
        else:
            end = (end + 1) % n
            if end == start:
                return start
            
    return -1


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.wave = ""
        self.left = left
        self.right = right

class Wavelet_Tree:
    def __init__(self, A: list[int]=[]):
        self.levels = None
        self.head = None
        if len(A) == 0:
            #print("Here")
            return None
        if len(A) == 1:
            self.head = Node(A[0])
        else:
            self.build(A)

    def build(self, A: list[int]):
        n = len(A)
        #print(sorted(A))
        #if len(A) == 2:
            #return Wavelet_Tree([0])
        if n % 2 == 0:
            median = sorted(A)[n//2]-1
        else:
            median = sorted(A)[n//2]
        #print("Median", median)
        left = []
        right = []
        newNode = Node(A)
        for i in A:
            if i <= median:
                newNode.wave += "0"
                left.append(i)
            else:
                newNode.wave += "1"
                right.append(i)
        newNode.left = Wavelet_Tree(left)
        newNode.right = Wavelet_Tree(right)
        self.head = newNode

    def get_wavelet_level_order(self):
        queueCur = []
        queueNext = []
        output = []
        queueCur.append(self)
        level = []
        while queueCur:
            hold = queueCur.pop(0)
            #print(hold.levels.data)
            #print(hold.levels)
            #print(hold.levels.wave)
            if hold.head.wave == "":
                level.append("X")
                #queueNext = []
            else:
                level.append(hold.head.wave)
            if hold.head.left != None:
                queueNext.append(hold.head.left)
                #print(hold.levels.left)
            if hold.head.right != None:
                queueNext.append(hold.head.right)
                #print(hold.levels.right)
            if len(queueCur) == 0:
                queueCur = queueNext
                queueNext = []
                output.append(level)
                level = []
        output.pop() #Removes that last index which isnt needed
        self.levels = output
        return output
    
    def RQQ(self, k:int, l:int, r:int):
        output = self.RQQHelper(k,l,r)
        output[1].insert(0, [k,l,r])
        return output

    def RQQHelper(self, k:int, l:int, r:int):
        #print(self.head.wave)
        hold = self.head.wave
        countZerosIn = 0
        countOnesIn = 0
        countZeroBefore = 0
        countOnesBefore = 0
        
        if hold == "":
            return [self.head.data, []]
        for i in range(0, r):
            if i < l-1:
                if hold[i] == '1':
                    countOnesBefore += 1
                else:
                    countZeroBefore += 1
            else:
                if hold[i] == '1':
                    countOnesIn += 1
                else:
                    countZerosIn += 1

        if countZerosIn >= k:
            l = countZeroBefore+1
            r = countZeroBefore+countZerosIn
            result = self.head.left.RQQHelper(k, l, r)
            result[1].insert(0, [k,l,r])
            return [result[0], result[1]]
        else:
            l = countOnesBefore+1
            r = countOnesBefore+countOnesIn
            k -= countZerosIn
            result = self.head.right.RQQHelper(k, l, r)
            result[1].insert(0, [k,l,r])
            return [result[0], result[1]]
            



        




if __name__ == "__main__":
    intervals = [[-3,-1],[-1,1],[-2,6]]
    print(maximum_intervals(intervals))
    d = [3, 4, 5, 1, 2]
    distance = [5, 5, 5, 5, 5]
    charging=[1, 2, 3, 4, 5]
    #print(circular_tour(distance, [1, 2, 3, 4, 5]))
    wv_tree = Wavelet_Tree([6, 2, 0, 7, 9, 3, 1, 8, 5, 4])
    print(wv_tree.get_wavelet_level_order())
    #print(wv_tree.get_wavelet_level_order())
    # Output: [['1001100110'], ['00101', '00110'], ['100', '01', '010', '10'], ['01', 'X', 'X', 'X', '10', 'X', 'X', 'X']]
    print(wv_tree.RQQ(5, 3, 9))


