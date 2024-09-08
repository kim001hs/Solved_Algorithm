import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n,m;
        n = sc.nextInt();
        m = sc.nextInt();
        for(int i=n; i<=m; i++){
            if(isPrime(i)) System.out.println(i);
        }

    }
    static boolean isPrime(int n){
        if(n<2) return false;
        for(int i=2; i*i<=n; i++){
            if(n%i==0) return false;
        }
        return true;
    }
}