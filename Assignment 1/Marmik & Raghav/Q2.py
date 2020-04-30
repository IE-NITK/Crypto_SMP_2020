# cook your dish here
def xor_strings(byte_1,byte_2):
    return bytes([a ^ b for a,b in zip(byte_1,byte_2)])
def raghav_marmik():
    byte_1 = bytes.fromhex(input("Enter the plain text"))
    byte_2 = bytes.fromhex(input("Enter the XOR key"))
    print("Cypher text = ",xor_strings(byte_1,byte_2).hex())

if __name__ == "__main__":
    raghav_marmik()
