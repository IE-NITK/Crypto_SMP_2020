# Assignment submission by SUSHANTH RAO: 191EE156, ADITYA KUMAR: 191CS104
import base64
import binascii

def hexadecimal_to_base64(string):
    proper_hex = True
    for b in string:
        if b not in '01234567890abcdef':
            proper_hex = False
    if proper_hex == True:
        ascii_str = binascii.unhexlify(string)
        converted_str = base64.b64encode(ascii_str)
        return converted_str
    else:
        return b'Invalid Hexadecimal string'

def fixed_xor(str1, str2):
    xor_str = ''
    byte_array_1 = bytearray.fromhex(str1)
    byte_array_2 = bytearray.fromhex(str2)
    xor_str = bytes().join([bytes([byte1 ^ byte2]) for byte1, byte2 in zip(byte_array_1, byte_array_2)])
    xor_str = binascii.hexlify(xor_str)
    return xor_str

def main():
    hex_to_b = input("Enter Hexadecimal string: ")
    converted = hexadecimal_to_base64(hex_to_b)
    print(converted.decode('utf-8'))
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")
    xored = fixed_xor(s1, s2)
    print(xored.decode('utf-8'))

if __name__ == "__main__":
    main()
