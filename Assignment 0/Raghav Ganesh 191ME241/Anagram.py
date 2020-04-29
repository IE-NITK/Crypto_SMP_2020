class crypto_smp:
    def anagram_logic(self,string1,string2,prime_numbers):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        #prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        d = dict(zip(alphabets,prime_numbers))
        #print(d)
        product_1 = 1
        product_2 = 1
        for i  in  string1:
            product_1 *= d[i]
        for i  in  string2:
            product_2 *= d[i]
        self.compare(product_1,product_2)
        
    def prime_fun(self,string1,string2):
        prime_numbers = []
        count = 0
        for num in range(2,102):
            for i in range(2,int(num/2)+1):
                    if num%i == 0:
                       break;
            else:
              prime_numbers.append(num)
        self.anagram_logic(string1,string2,prime_numbers)
    def compare(self,a,b):
        if(a == b):
            print("This two strings are anagram")
        else:
            print("These are not anagrams")

    def input_strings(self):
        string1 = input()
        string2 = input()
        self.prime_fun(string1,string2)
if __name__ == "__main__":
    obj1=crypto_smp()
    obj1.input_strings()
