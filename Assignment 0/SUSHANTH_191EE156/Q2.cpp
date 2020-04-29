//Time Complexity of the following algorithm is O(logn)
//Prime Factors are computed using Sieve Of Eratosthenes(ancient) algorithm.
#include<bits/stdc++.h> 
using namespace std; 

void primeFactors(int N, int s[]) 
{ 
    vector <bool> prime(N+1, false); 
  
    for (int i=2; i<=N; i+=2) 
        s[i] = 2; 
  
    for (int i=3; i<=N; i+=2) 
    { 
        if (prime[i] == false) 
        {  
            s[i] = i; 
   
            for (int j=i; j*i<=N; j+=2) 
            { 
                if (prime[i*j] == false) 
                { 
                    prime[i*j] = true; 
                    s[i*j] = i; 
                } 
            } 
        } 
    } 
} 
  
void generatePrimeFactors(int N) 
{ 
    int s[N+1]; 
    int num_factors = 1;
    unordered_map<int, int> expo;
    primeFactors(N, s); 
    int curr = s[N];
    while (N > 1) 
    { 
        N /= s[N]; 
  
        if (curr == s[N]) 
        { 
            expo[curr]++; 
            continue; 
        } 
        expo[curr]++; 
        num_factors*=(1 + expo[curr]);
        curr = s[N]; 
    }
    printf("%d",num_factors);
} 
  
int main() 
{ 
    int N;
    std::cin >> N;
    generatePrimeFactors(N); 
    return 0; 
} 
