package assignment0;

import java.util.Scanner;

public class num_of_factors {
    private int count;

    public num_of_factors(long n){
        if(n<1)
            throw new IllegalArgumentException("Enter a number greater than 0");
        if(n==1)
            count = 1;
        else
            count = 2;
        double root=Math.pow(n,0.5);
        for(long i=2;i<=root;i++)
        {
            if(i==root)
                count++;
            if(n%i==0&&i!=root)
                count+=2;
        }
    }

    public long count(){
        return count;
    }

    public static void main(String[] args) {
        System.out.println("Enter the number");
        Scanner sc=new Scanner(System.in);
        long n=sc.nextLong();
        num_of_factors obj=new num_of_factors(n);
        System.out.printf("Number of factors = %d",obj.count());
    }
}

