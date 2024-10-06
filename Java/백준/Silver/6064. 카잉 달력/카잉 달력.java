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
            //나머지는 0이 될 수 있고 x와y는 1부터 시작하기 때문에 1씩 빼서 계산한 후 나중에 결과에 1을 더해준다
            
            int lcm = M * N / GCD(M, N);//최소공배수
            int year=x;
            //year을  x부터 시작해서 M씩 증가시키면서 year%N==y가 될때까지 반복
            while(!(year%N==y)){
                year+=M;
                if(year>lcm){//year이 lcm보다 커지면 불가능한 경우이므로 반복문을 종료
                    year=-2;
                    break;
                }
            }
            System.out.println(year+1);
        }
    }
    public static int GCD(int a, int b){//최대공약수
        if(b==0) return a;
        return GCD(b,a%b);
    }
}