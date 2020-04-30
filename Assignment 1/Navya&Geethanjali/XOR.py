def encode_XOR(bytes_string, key_string):
    result = ''
    bit_list = list(''.join([bin(byte)[2:].zfill(8) for byte in bytes_string]))
    key_list = list(''.join([bin(byte)[2:].zfill(8) for byte in key_string]))
    bit_list = ''.join(bit_list)
    key_list = ''.join(key_list)
    
    i = 0
    while( len(key_list) < len(bit_list)):
        key_list.append(bit_list[i])
        i += 1
        
    for x in range(len(bit_list)):
        if bit_list[x] == key_list[x]:
            result += '0'
        else:
            result += '1'
   
    decoded = hex(int((result),2))        
    return decoded[2:]

input_hex = input("Enter hex string: ");
byte_string = bytes.fromhex(input_hex);
input_hex = input("Enter hex string: ");
key_string = bytes.fromhex(input_hex);

print(encode_XOR(byte_string, key_string))