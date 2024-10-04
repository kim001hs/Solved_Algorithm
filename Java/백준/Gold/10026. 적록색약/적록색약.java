import java.io.IOException;
import java.util.Scanner;

public class Main{
    static char s[][];
    static boolean visited[][];
    static int count=0;
    static int dx[]={1,-1,0,0};
    static int dy[]={0,0,1,-1};
    static int n;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        s=new  char[n][n];
        visited=new boolean[n][n];
        for(int i=0; i<n; i++){
            String input=sc.next();
            for(int j=0; j<n; j++){
                s[i][j]=input.charAt(j);
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(!visited[i][j]){
                    dfs(i,j);
                    count++;
                }
            }
        }
        int count1 = count;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(s[i][j]=='G'){
                    s[i][j]='R';
                }
            }
        }
        count=0;
        visited=new boolean[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(!visited[i][j]){
                    dfs(i,j);
                    count++;
                }
            }
        }
        int count2 = count;
        System.out.println(count1+" "+count2);
    }
    public static void dfs(int cy,int cx){
        visited[cy][cx]=true;
        for(int i=0;i<4;i++){
            int ny=cy+dy[i];
            int nx=cx+dx[i];
            if(ny>=0&&ny<n&&nx>=0&&nx<n&&s[ny][nx]==s[cy][cx]&&!visited[ny][nx]){
                dfs(ny,nx);
            }
        }
    }
}