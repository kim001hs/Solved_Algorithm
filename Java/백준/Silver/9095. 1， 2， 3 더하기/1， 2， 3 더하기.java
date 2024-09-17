import java.io.IOException;
import java.util.Scanner;

public class Main{
    static int dp[] = new int [11];
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        dp[1]=1; //초기 값 초기화
		dp[2]=2;
		dp[3]=4;
		
		for(int j=4;j<=10;j++) { // 4부터 반복
			dp[j] = dp[j-3] + dp[j-2] + dp[j-1]; // 점화식
		}
		
		for(int i=0;i<n;i++) {
			int temp = sc.nextInt();
			System.out.println(dp[temp]);
		}
    }
}