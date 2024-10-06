import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        for (int i = 0; i < n; i++) {
            int M = sc.nextInt();
            int N = sc.nextInt();
            int x= sc.nextInt()-1;
            int y= sc.nextInt()-1;
            int year=x;

            int lcm = M * N / GCD(M, N);

            while(!(year%N==y)){
                year+=M;
                if(year>lcm){
                    year=-2;
                    break;
                }
            }
            System.out.println(year+1);
        }
    }
    public static int GCD(int a, int b){
        if(b==0) return a;
        return GCD(b,a%b);
    }
}