box = { 'a': 2, 'b' : 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 
        'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67,
        't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 87, 'y': 89, 'z': 97 }

word1, word2 = input("--"), input("--")
pdt1, pdt2 = 1, 1
if len(word1) == len(word2):
    for i in word1:
        pdt1 ^= box[i]
    for i in word2:
        pdt2 ^= box[i]
    if pdt1 == pdt2:
        print("ANAGRAM")
    else:
        print("Not an ANAGRAM")
else:
    print("Not an ANAGRAM")
