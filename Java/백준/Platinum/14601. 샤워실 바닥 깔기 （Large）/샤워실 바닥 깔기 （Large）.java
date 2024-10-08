import java.io.IOException;
import java.util.Scanner;

public class Main{
    static int[][] arr;
    static int num=0;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int k=sc.nextInt();
        int n=1;
        for(int i=0;i<k;i++){
            n*=2;
        }
        arr = new int[n+1][n+1];
        int x=sc.nextInt();
        int y=n-sc.nextInt()+1;
        arr[y][x]=-1;
        solve(1,1,n);

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void solve(int y, int x, int size){
        num++;
        int half_size=size/2;
        if(isInside(y, x, half_size))arr[y+half_size-1][x+half_size-1]=num;
        if(isInside(y+half_size, x, half_size))arr[y+half_size][x+half_size-1]=num;
        if(isInside(y, x+half_size, half_size))arr[y+half_size-1][x+half_size]=num;
        if(isInside(y+half_size, x+half_size, half_size))arr[y+half_size][x+half_size]=num;

        if(size==2)return;

        solve(y, x, half_size);
        solve(y, x+half_size, half_size);
        solve(y+half_size, x, half_size);
        solve(y+half_size, x+half_size, half_size);

    }
    public static boolean isInside(int y, int x, int size){
        for(int i=y;i<y+size;i++){
            for(int j=x;j<x+size;j++){
                    if(arr[i][j]!=0){
                        return false;
                }
            }
        }
        return true;
    }
}