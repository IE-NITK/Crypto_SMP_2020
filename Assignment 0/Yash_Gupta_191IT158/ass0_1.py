s1=input()
s2=input()
if len(s1)!=len(s2):
    print("Not Anagrams")
else:
    x=0
    for i in range(len(s1)):
        x=x^ord(s1[i])^ord(s2[i])
    if x==0:
        print("Anagrams")
    else:
        print("Not Anagrams")
    