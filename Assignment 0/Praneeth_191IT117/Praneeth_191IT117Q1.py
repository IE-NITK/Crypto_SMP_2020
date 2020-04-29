d={
        "a":2,
        "b":3,
        "c":5,
        "d":7,
        "e":11,
        "f":13,
        "g":17,
        "h":19,
        "i":23,
        "j":29,
        "k":31,
        "l":37,
        "m":41,
        "n":43,
        "o":47,
        "p":53,
        "q":59,
        "r":61,
        "s":67,
        "t":71,
        "u":73,
        "v":79,
        "w":83,
        "x":89,
        "y":97,
        "z":101,
        " ":1
}
s1=input("Enter the string1\n")
s2=input("Enter the string2\n")
s1=list(s1)
s2=list(s2)
m=1
n=1
for i in s1:
        m=m*d[i]
for i in s2:
        n=n*d[i]
if n==m:
        print("They are anagrams")
else:
        print("They are not anagram")
