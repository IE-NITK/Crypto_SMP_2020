/*it would have been way simpler if sorting of the two strings was allowed*/
package assignment0;
import java.util.*;
public class anagram {

    public boolean check(String str1,String str2){
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        if(str1.length()==str2.length()) {
            int length=str1.length();
            for (int i = 0; i < length; i++) {
                char a = str1.charAt(i);
                for(int j = 0;j < length; j++){
                    if(str2.charAt(j)==a){
                        str2=charRemoveAt(str2,j);
                        break;
                    }
                }
            }
            return str2 == null;
        }
        else return false;
    }

    public String charRemoveAt(String str, int p) {
        if(str.length()>1)
            return str.substring(0, p) + str.substring(p + 1);
        else
            return null;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter string 1");
        String str1=sc.next();
        System.out.println("Enter string 2");
        String str2=sc.next();
        anagram obj=new anagram();
        System.out.print("The two entered strings are anagram : " + obj.check(str1,str2));
    }
}
