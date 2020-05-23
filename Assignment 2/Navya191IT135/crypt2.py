input_hex = input("Enter hex string: ")
lst = []
new_lst = []
xor_lst1 = []
xor_lst2 = []
score = 0
highscore = 0
final = []
l = 0
x = len(input_hex)

# Splitting hex string in groups of 2 characters
for i in range(0,x,2):
    lst.append(input_hex[i:i+2])
    
# Converting each hexadecimal character to binary
for i in range(int(x/2)):
    new_lst.append(bin(int(lst[i],16))[2:].zfill(8))
    
for i in range(int(x/2)):
    final.append('')
    
# Frequency chart of characters appearing in English
char_lst = {97: 0.08497, 	
            98: 0.01492, 	
            99: 0.02202, 	
            100: 0.04253, 	
            101: 0.11162, 	
            102: 0.02228, 	
            103: 0.02015, 	
            104: 0.06094,
            105: 0.07546,	
            106: 0.00153,	
            107: 0.01292, 	
            108: 0.04025, 	
            109: 0.02406, 	
            110: 0.06749, 	
            111: 0.07507,	
            112: 0.01929,
            113: 0.00095, 	
            114: 0.07587,  
            115: 0.06327, 	
            116: 0.09356, 	 
            117: 0.02758,
            118: 0.00978,
            119: 0.02560, 	
            120: 0.00150, 	
            121: 0.01994, 	
            122: 0.00077,
            32: 0.13000}
    
key = []

# Making a list of all possible keys
for i in range(256):
    key.append(bin(i)[2:].zfill(8))
    
# XOR with every possible key and finding highest score
for i in range(256):
    for j in range(int(x/2)):
        for k in range(8):
            xor_lst1.append(str(int(new_lst[j][k])^int(key[i][k])))
        xor_lst2.append(''.join(xor_lst1))
        xor_lst1 = []
    for q in xor_lst2:
        p = int(q,2)
        if p in char_lst:
            score += char_lst[p]
    if score >= highscore:
        highscore = score
        for y in range(int(x/2)):
            final[y] = xor_lst2[y]
    xor_lst2 = []
    score = 0
    
# Printing final answer
for q in final:
    p = int(q,2)
    print("{:c}".format(p), end = "")