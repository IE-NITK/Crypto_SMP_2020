//Time Complexity Of Computing Prime Numbers Is O(n*log(log(n)))
//Prime Numbers is computed using Sieve Of Eratosthenes(ancient) algorithm.
//(Logic) - Prime numbers multiplied to different integers cannot yield the same result.

#include <bits/stdc++.h> 
using namespace std;
int prime_num[26];
string s1,s2;
int prime_product_1 = 1;
int prime_product_2 = 1;
int len_1 = 0;
int len_2 = 0;
void SieveOfEratosthenes(int n) 
{ 
     
    bool prime[n+1]; 
    memset(prime, true, sizeof(prime)); 
  
    for (int p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        {   
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
  
    for (int p=2,i=0; p<=n; p++){
        if (prime[p]){
           prime_num[i] = p;
           i++;
       }
    }
    
       for(int i=0;i<len_1;i++){
           prime_product_1 *= prime[s1[i] - 'a'];
           prime_product_2 *= prime[s2[i] - 'a'];
       }
       if(prime_product_1 == prime_product_2)
       cout << "Anagrams\n";
       else
       cout << "Not Anagrams\n";
        
} 
  
int main() 
{ 
    int n = 102;
    cout << "Enter two strings\n";
    cin >> s1 >> s2;
    for(int i=0;i>=0;i++){
        if(s1[i] == '\0')
        break;
        len_1++;
    }
    for(int i=0;i>=0;i++){
        if(s2[i] == '\0')
        break;
        len_2++;
    }
    if(len_1 == len_2){
        SieveOfEratosthenes(n);
    }
    else
    cout << "Not Anagrams\n"; 
    return 0; 
} 
