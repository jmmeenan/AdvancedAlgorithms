class amor_dict():
    def __init__(self, num_list = []):
        # your code here
        self.allArrays = {}
        for i in num_list:
            self.insert(i)
        
    def insert(self, num):
        # your code here
        hold = [num]
        index = 0
        while index < len(self.allArrays):
            if self.allArrays[index] == []:
                break
            else:
                hold += self.allArrays[index]
                self.allArrays[index] = []
                index += 1
                hold.sort()
        self.allArrays[index] = hold

    def search(self, num):
        # your code here
        level = 0
        while level < len(self.allArrays):
            for i in self.allArrays[level]:
                if i == num:
                    return level
            level += 1
        return -1
    
    def print(self):
        # your code here
        output = []
        if len(self.allArrays) == 0:
            return [[]]
        for i in self.allArrays:
            output.append(self.allArrays[i])
        return output

def implement_queue(operations):
    output_list = []
    stack1 = []
    stack2 = []
    for i in operations:
        command = i.split("(")
        com = command[0]

        if com == "push":
            number = command[1].split(")")
            num = number[0]
            stack1.append(int(num))

        if com == "peek":
            if(stack1 == [] and stack2 == []):
                output_list.append("#")
            else:
                if len(stack2) == 0:
                    while stack1 != []:
                        hold = stack1.pop()
                        stack2.append(hold)
                output_list.append(stack2[len(stack2)-1])

        if com == "pop":
            if(stack1 == [] and stack2 == []):
                output_list.append("#")
            else:
                if len(stack2) == 0:
                    while stack1 != []:
                        hold = stack1.pop()
                        print(hold)
                        stack2.append(hold)
                output_list.append(stack2.pop())

        if com == "empty":
            output_list.append(stack1 == [] and stack2 == [])

    
    
    return output_list


if __name__ == "__main__":
    operations = ["push(1)", "push(2)", "peek()", "pop()", "empty()", "pop()", "empty()"]
    print(implement_queue(operations))

    ad = amor_dict([23, 12 ,24, 42])
    print(ad.print())
    # [[], [], [12, 23, 24, 42]]
    ad.insert(11)
    print(ad.print())
    # [[11], [], [12, 23, 24, 42]]
    ad.insert(74)
    print(ad.print())
    # [[], [11, 74], [12, 23, 24, 42]]
    print(ad.search(74))
    # 1
    print(ad.search(77))
    # -1
    ad = amor_dict([])
    print(ad.print())