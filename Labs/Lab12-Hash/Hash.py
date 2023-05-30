def hash_string(s):
    output = 0
    for i in range(len(s)):
        output = (output * 26 + (ord(s[i]) - 96)) % 1009
    return output

def is_substring(s1 : str, s2 : str) -> bool:
    n = len(s1)
    m = len(s2)
    
    if n > m:
        return False
    
    hashS1 = hash_string(s1)
    hashS2 = hash_string(s2[:n])
    
    if hashS1 == hashS2:
        if s1 == s2[:n]:
            return True
    
    for i in range(n, m):
        hashS2 = (hashS2 - (ord(s2[i - n]) - 98) * (26 ** (n - 1))) % 1009
        hashS2 = (hashS2 * 26 + (ord(s2[i]) - 96)) % 1009
        if hashS1 == hashS2:
            if s1 == s2[i - n + 1:i + 1]:
                return True
    return False

if __name__ == "__main__":
    
    print(hash_string("cat"))
    print(hash_string("toys"))
    print(is_substring("cat", "cats"))
    print(is_substring("toy", "toys are us"))
    print(is_substring("oat", "tao of life"))