
#Angrams Checking
def is_anagram(s1, s2):
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    p1 = 1
    for i in s1:
        x = ord(i) - 97;
        p1 *= arr[x]
    p2 = 1
    for i in s2:
        x = ord(i) - 97;
        p2 *= arr[x]
    if p1 == p2:
        return True
    else:
        return False
#Main Program
print("Enter two texts:")
s1= input()
s2 = input()
#Changing to lower cases
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
#Checking anagram
bool=is_anagram(s1,s2)
if(bool==True):
    print("Anagrams")
else:
    print("Not Angrams")