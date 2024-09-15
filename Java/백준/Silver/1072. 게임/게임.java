import java.io.IOException;
import java.util.Scanner;

public class Main{
    static int  x,y,z;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        x = sc.nextInt();
        y = sc.nextInt();
        z = (int)((long) y * 100 / x);
        if(z>=99){
            System.out.println(-1);
            return;
        }
        else{
            binarySearch();
        }
    }
    public static void binarySearch() {
        int left = 1;
        int right = x;
        while(left<=right){
            int mid=(left+right)/2;
            int changedZ = (int)(((long)(y + mid) * 100) / (x + mid));
            if(changedZ!=z){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        System.out.println(left);
    }
}