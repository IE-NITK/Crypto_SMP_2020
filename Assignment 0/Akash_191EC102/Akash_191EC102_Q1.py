def isprime(num):
    factors=0
    for i in range(1,num+1):
        if (num%i==0):
            factors=factors+1
    if (factors==2):
        return True
    else:
        return False
    
def next_prime_generator(current_prime):
    generated=0
    counter=current_prime+1
    while (not generated):
        if isprime(counter):
            generated=1
            return counter
        else:
            counter=counter+1
            
def length(l):
    count=0
    for i in l:
        count=count+1
    return count

def assign_prime(list1,list2):
    current_prime=10
    marked1=[0 for x in list1]
    marked2=[0 for x in list2]
    count=0
    for i in list1:
        if marked1[count]:
            count=count+1
            continue
        temp=i
        marked1[count]=1
        current_prime=next_prime_generator(current_prime)
        list1[count]=current_prime
        j=count+1
        while (j<=length(list1)-1):
            if (list1[j]==temp):
                list1[j]=current_prime
                marked1[j]=1
            j=j+1
        count1=0
        for j in list2:
            if list2[count1]==temp and marked2[count1]!=1:
                list2[count1]=current_prime
                marked2[count1]=1
            count1=count1+1
        count=count+1
    for i in marked1:
        if i==0:
            return 0
    for i in marked2:
        if i==0:
            return 0
    prod1=1
    prod2=1
    for i in list1:
        prod1*=i
    for i in list2:
        prod2*=i
    if (prod1==prod2):
        return 1
    else :
        return 0
def check_anagram(str1,str2):
    list1=[x for x in str1]
    list2=[x for x in str2]
    if (assign_prime(list1, list2)):
        print("The two strings are anagrams")
    else:
        print("The two strings are not anagrams")
def input_string():
    str1=input("Enter string 1 : ")
    str2=input("Enter string 2 : ")
    check_anagram(str1, str2)
input_string()
        
        
        
    
