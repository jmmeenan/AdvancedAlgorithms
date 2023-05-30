from typing import List


def is_prime(m : int)-> bool:
    i = m//2
    if m == 0 or m == 1:
        return False
    else:
        while i > 1:
            if m % i == 0:
                return False
            i-=1
        return True
    return False

def primes(n : int) -> List[int]:
    i = 2
    list = []
    while i < n:
        if is_prime(i) is True:
            list.append(i)
        i+=1
    return list




if __name__ == '__main__':
    print(primes(3))


