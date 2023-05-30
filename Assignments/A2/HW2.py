def postfix_string(arr):
    stack = []
    if len(arr) == 0:
        return ""
    for i in arr:
        #num = ord(i)
        if(isinstance(i, int)):
            stack.append(int(i))
        elif i == "-":
            number = stack.pop()
            s = stack.pop()
            s = s[0:int(number)] + s[int(number)+1:]
            stack.append(s)
            #-----
        elif i == "*":
            number = stack.pop()
            s = stack.pop()
            stack.append(s*int(number))
            #*****
        elif i == "+":
            s2 = stack.pop()
            s1 = stack.pop()
            stack.append(s1 + s2)
            #++++++
        else:
            stack.append(i)
    return stack[0]

class ListNode():
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class AstronomicalInt():
  def convert(self, num:str) -> ListNode:
    # Returns head of linked list
    if num == []:
        return None
    if num == None:
        return None
    count = len(num)-1
    if count <= 0:
        return 0
    output = ListNode(num[count], None)
    count -= 1
    while count >= 0:
        output = ListNode(num[count], output)
        count -= 1
    return output

  def add(self, num1:ListNode, num2: ListNode) -> ListNode:
    # Returns head of new linked list after adding the given lists
    if num1 == [] and num2 == []:
        return 0
    if num1 == []:
        return num2
    if num2 == []:
        return num2
    n1 = self.to_string(num1)
    n2 = self.to_string(num2)
    total = int(n1) + int(n2)
    return self.convert(str(total))

  def to_string(self, head):
    num = []
    curr = head
    while curr:
        num.append(curr.val)
        curr = curr.next
    num = ''.join([str(i) for i in num])
    return num

def countAtoms(formula):
    number = "" 
    formula += " "
    stack = [1]
    lowerLetter = ""
    d = {}
    i = len(formula) - 2
    
    while i >= -1:
        cur = ord(formula[i])
        fullElement = formula[i] + lowerLetter
        if cur >= 48 and cur <= 57:
            number = fullElement + number
            i -= 1
            continue
        elif cur >= 97 and cur <= 122:
            lowerLetter = fullElement + lowerLetter
            i -= 1
            continue
        elif cur == 41:
            stack.append(stack[-1] * int(number))
            number = ''
            i -= 1
            continue
        elif cur == 40:
            stack.pop()
            i -= 1
            continue
        total = d.get(fullElement, 0)
        if number == "":
            total += stack[-1]
        else:
            total += stack[-1]*int(number)
        d[fullElement] = total
        lowerLetter = ""
        number = ""
        i -= 1
    
    result = ""
    for i, j in sorted(d.items()):
        if i == " ":
            continue
        result += i
        if j != 1:
            result += str(j)
    return result


def combination_check(n,st):
    s1 = ""
    d = {}
    count = 0
    n2 = str(n)
    index = 0
    while index < len(st):
        if count > len(n2)-1:
            return False
        if st[index] != " ":
            s1 += st[index]
        if st[index] == " " or (index == len(st)-1):
            #print()
            #print(s1)
            #print(n2[count])
            #print()
            if d.__contains__(s1):
                if d[s1] != n2[count]:
                    return False
            else:
                #print(n2[count] in d.values())
                if n2[count] in d.values():
                    #print(d)
                    #print(d.__contains__("dog"))
                    return False
                else:
                    d[s1] = n2[count]
            s1 = ""
            count += 1
        index+=1
    return True

def diff_max_min(arr):
    totalMax = 0
    totalMin = 0
    for i in range(len(arr) + 1):
        for j in range(i):
            hold = arr[j: i]
            totalMax += max(hold)
            totalMin += min(hold)
    return totalMax - totalMin



if __name__ == '__main__':
    print("Postfix_string Tests")
    print(postfix_string("ab+5*7-"))
    print(postfix_string("a2*b5*+"))
    print(postfix_string(["abcde",3,"-"]))

    print()
    print("ListNode Tests")
    ast = AstronomicalInt()
    n1 = ast.convert("1234")
    n4 = ast.convert([])
    n2 = ast.convert("16")
    n3 = ast.add(n1, n2)
    print(ast.to_string(n3)) # Output: 1250

    print()
    print("Formula Tests")
    print(countAtoms("H2O"))
    print(countAtoms("K4(ON(SO3)2)2"))
    print(countAtoms("K4(Fe(CN)6)"))

    print()
    print("Combination check tests")
    print(combination_check(1221, "horse radish horse cat"))
    print(combination_check(1212, "horse fish horse fish"))
    print(combination_check(122122, "Ape dog dog Ape dog dog"))
    print(combination_check(12312, "bat cat box bat dog rabbit"))
    print(combination_check(123123, "dog cat robot dog cat Robot"))
    print(combination_check(213213, "dog cat rabbit dog Cat rabbit"))
    print(combination_check(1111, "dog dog dog dog dog dog"))

    print()
    print("Max min tests")
    print(diff_max_min([1,2,3,4]))
    print(diff_max_min([3,1,2]))

