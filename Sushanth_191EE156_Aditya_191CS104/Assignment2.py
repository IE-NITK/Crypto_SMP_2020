# Assignment submission by SUSHANTH SATHESH RAO - 191EE156 & ADITYA KUMAR - 191CS104

# The best possible message has been found by character frequency technique.
# Data for letter scoring has been picked from Wikipedia.
def xor_score(char, input):
    message_score = {}
    output = b''
    for byte in input:
        output += bytes([byte ^ char])
    message_score["message"] = output
    character_frequency = {
        'a': .08497, 'b': .01492, 'c': .02202, 'd': .04253, 'e': .11162, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .07546, 'j': .00153, 'k': .01292, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .07587, 's': .06327, 't': .09356, 'u': .02758, 'v': .00978, 'w': .02560, 'x': .00150, 'y': .01994, 'z': .00077, ' ': .13000
    }
    score = 0
    for byte in output.lower():
        score += character_frequency.get(chr(byte), 0)
    message_score["score"] = score
    message_score["key"] = char
    return message_score

def best_possible_message(string):
    possible_messages = []
    for ascii_char in range(128):
        message_score = xor_score(ascii_char, string)            
        possible_messages.append(message_score)
    max_score = sorted(possible_messages, key = lambda x: x['score'], reverse = True)[0]
    return max_score

def guess_the_string():
    data_of_file = open('/home/decoder/challenge4.txt').read().splitlines()
    possible_encrypted_messages = []
    line = 0
    for hex in data_of_file:
        line += 1
        dictionary = best_possible_message(bytes.fromhex(hex))
        dictionary["line"] = line
        possible_encrypted_messages.append(dictionary)
    max_score = sorted(possible_encrypted_messages, key = lambda x: x['score'], reverse = True)[0]
    print(max_score["message"].decode('utf-8').replace('\n',''))
    print('Line: {}'.format(max_score["line"]))
 
def main():
    input_hex = input("Enter hexadecimal string\n")
    proper_hex = True
    for char in input_hex:
        if char not in '0123456789abcdef':
            proper_hex = False
    if proper_hex == True:
        string = bytes.fromhex(input_hex)
        print(best_possible_message(string)["message"].decode('utf-8'))
        guess_the_string()
    else:
        print("Invalid hexadecimal string")            
    
if __name__ == '__main__':
    main()