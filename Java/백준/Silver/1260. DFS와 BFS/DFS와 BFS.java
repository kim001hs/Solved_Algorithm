import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main{
    static boolean  map[][];
    static boolean visited[];
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        int M=sc.nextInt();
        int V=sc.nextInt();
        map=new boolean[N+1][N+1];
        visited=new boolean[N+1];
        for(int i=0;i<M;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            map[a][b] = true;
            map[b][a] = true;
        }
        dfs(V);
        System.out.println();
        visited=new boolean[N+1];
        bfs(V);
    }
    public static void dfs(int V){
        visited[V]=true;
        System.out.print(V+" ");
        for(int i=1;i<map.length;i++){
            if(map[V][i] && !visited[i]){
                dfs(i);
            }
        }
    }
    public static void bfs(int V){
        visited[V]=true;
        Queue<Integer> q = new LinkedList<>();
        q.add(V);
        while(!q.isEmpty()){
            int temp=q.poll();
            System.out.print(temp+" ");
            for(int i=1;i<map.length;i++){
                if(map[temp][i] && !visited[i]){
                    q.add(i);
                    visited[i]=true;
                }
            }
        }
    }
}