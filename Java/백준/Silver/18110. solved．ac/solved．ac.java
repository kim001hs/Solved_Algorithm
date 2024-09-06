import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double sum=0;
        int n = Integer.parseInt(br.readLine());
        int cut=(int) Math.round(n * 0.15);
        int[] arr = new int[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        for(int i = cut; i < n-cut; i++){
            sum+=arr[i];
        }

        int avg=(int) Math.round(sum/(n-2*cut));
        System.out.println(avg);
    }
}