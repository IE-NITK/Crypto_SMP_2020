ref_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

input_hex = input("Enter hex string: ");
byte_string = bytes.fromhex(input_hex);
output = ""

lst = []
new_lst = []

for i in byte_string:
    for j in bin(i)[2:].zfill(8):
        lst.append(j)

i = 0
while i < len(lst):
  new_lst.append(lst[i:i+6])
  i+=6
  
for i in new_lst:
    i = ''.join(i)
    if len(i) == 2:
            if '1' in i:
                i += '0000'
                output += ref_table[int(i, 2)] + '=='
            else:
                output += '=='
    elif len(i) == 4: 
            if '1' in i:
                i += '00'
                output += ref_table[int(i, 2)] + '='
            else:
                output += '='
    elif len(i) == 6:
            output += ref_table[int(i, 2)]
            
print(output)