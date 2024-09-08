import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int result=0;
        while(n%5!=0){
            n-=3;
            result++;
            if(n<0){
                System.out.println(-1);
                return;
            }
        }
        result+=n/5;
        System.out.println(result);
    }
}
