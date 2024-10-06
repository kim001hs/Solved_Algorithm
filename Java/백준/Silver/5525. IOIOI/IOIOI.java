import java.io.IOException;
import java.util.Scanner;

public class Main{
    static String S;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        S = sc.next();

        int count = 0;
        int[] memo = new int[M];

        for(int i=1; i<M-1; i++){
            if(S.charAt(i)=='O'&&S.charAt(i+1)=='I'){
                memo[i+1] = memo[i-1]+1;
                if(memo[i+1]>=N&&S.charAt(i+1-2*N)=='I'){
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}