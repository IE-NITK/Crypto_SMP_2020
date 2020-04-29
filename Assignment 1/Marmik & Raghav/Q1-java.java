package assignment1;
import java.math.BigInteger;
import java.util.*;
public class hex_to_base64   {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the string :");
        String hex=sc.next();
        String base64 = Base64.getEncoder().encodeToString(new BigInteger(hex, 16).toByteArray());
        System.out.println(base64);
    }
}

