s=int (input("Enter the first string\n"),16)
t=int(input("Enter the second srting\n"),16)
print("The answer is :\n",hex(s^t).replace("0x",""))
