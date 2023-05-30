

def depthStack(s: str) -> int :
    if s == "":
        return 0
    if s == "()":
        return 1
    stack = []
    m = 0
    rm = 0
    for i in s:
        if i == "(":
            stack.append(i)
            if(m == rm):
                m += 1
                rm += 1
            
        if i == ")":
            stack.pop()
            rm -= 1
    return m

def depth(s: str) -> int :
    if s == "":
        return 0
    if s == "()":
        return 1
    left = ""
    right = ""
    index = 0
    o = 0
    c = 0
    for i in s:
        index += 1
        left += i
        if i  == "(":
            o += 1
        if i == ")":
            c += 1
        if o == c:
            if index == len(s)-1:
                return c
            break
    right = s[index:]
    a = 1 + depth(left[1:len(left)-1])
    b = depth(right)
    return max(a, b)
    

if __name__ == '__main__':
    print(depthStack("()(())"))