import base64
def hexToBase64(s):
    decodedString = bytes.fromhex(s)
    print("Plain text is = ",decodedString)
    base64EncodedString = base64.b64encode(decodedString)
    return base64EncodedString.decode()
    
if __name__ == "__main__":
    s = input("Enter string to be converted\n")
    cyphertext = hexToBase64(s)
    print("Cypher text is = ",cyphertext)
