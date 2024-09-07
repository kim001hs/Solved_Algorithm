import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int m=sc.nextInt();
        for(int i = 0; i < m; i++){
            int temp=sc.nextInt();  
            if (Arrays.binarySearch(arr, temp) >= 0) {
                System.out.println("1");
            } else {
                System.out.println("0");
            }
        }
    }
}