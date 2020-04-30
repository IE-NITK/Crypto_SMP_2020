package assignment1;
import java.math.BigInteger;
import java.util.*;
public class Fixed_XOR {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string1 :");
        String str1 = sc.next();
        System.out.println("Enter the string2 :");
        String str2 = sc.next();
        BigInteger s1=new BigInteger(str1,16);
        BigInteger s2=new BigInteger(str2,16);
        BigInteger xor=s1.xor(s2);
        String ans=xor.toString(16);
        System.out.println(ans);
    }
}
