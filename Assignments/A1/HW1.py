from array import *
import math

#test

def get_distance(arr):
    total = 0
    index = 0
    n = 0
    if arr == [] or len(arr) == 1:
        return 0
    while index < len(arr):
        n += 1
        for i in arr[index:]:
            hold = arr[index] ^ i
            total += (bin(hold).count("1")*2)
            n += 1
        index += 1
    print(n)
    return total

def sumnation(n, l):
    if n == 0:
        return 0
    if n == l: 
        return l
    else:
        return n + sumnation(n-1, l)

def move_steps(k):
    output = 0
    if k == 0:
        return 0
    ones = k
    twos = 0
    while ones >= 0:
        output += math.factorial(ones+twos)/(math.factorial(twos)*math.factorial(ones))
        twos += 1
        ones -= 2
    return int(output)

def decode_message(s):
    output = ""
    if s == "":
        return s
    index = 0
    switch = 0
    while index < len(s):
        if index % 2 == (switch % 2):
            output += s[index]
            index += 1
        else:
            if index == (len(s) - 1):
                output += s[index]
                return output
            if s[index] != s[index + 1]:
                return s
            else:
                switch += 1
                output += s[index]
            index += 2
    return output

def count_sub_strs(s: str) ->int:
    output = 0
    f1 = 0
    f2 = 0
    r = 1
    while f2 != -1:
        f2 = s.count("b"*r + "a" *r)
        f1 = s.count("a"*r + "b" *r)
        output += f2
        output += f1
        r += 1
        if(r > len(s)):
            f2 = -1
    
    return output
            

def check_transformation(s1, s2):
    if len(s1) != len(s2):
        return False
    chars1 = {}
    chars2 = {}
    index = 0
    while index < len(s1):
        if chars1.__contains__(s1[index]):
            if chars1.get(s1[index]) != s2[index]:
                return False
        if chars2.__contains__(s2[index]):
            if chars2.get(s2[index]) != s1[index]:
                return False
        else:
            chars1[s1[index]] = s2[index]
            chars2[s2[index]] = s1[index]
        index += 1
    return True


if __name__ == '__main__':
    #binary Test 
    print("Binary Test")
    test1 = [2,3,4]
    print(get_distance(test1))
    test2 = [52, 78]
    print(get_distance(test2))
    test3 = [52, 78, 100]
    print(get_distance(test3))

    #k step test
    print("K step Test")
    print(move_steps(1))
    print(move_steps(0))
    print(move_steps(2))
    print(move_steps(3))
    print(move_steps(36))
    print(move_steps(24))
    print(move_steps(23))

    # dexode_message test
    print("Decode message tests")
    print(decode_message("SEECRRETTMEESSSAGGE"))
    print(decode_message("toomaatoo"))
    print(decode_message(""))
    print(decode_message("hi"))
    print(decode_message("this is a test"))

    #count sub strings tests
    print("count substrings test")
    print(count_sub_strs("aabbaabb"))
    print(count_sub_strs("abaaaa"))
    print(count_sub_strs("aabaabb"))

    # check transformation
    print("Check transformation tests")
    print(check_transformation("bdba", "bcbc"))
    print(check_transformation("abb", "abc"))
    print(check_transformation("odd", "iff"))
    print(check_transformation("rmnbhv", "abacde"))