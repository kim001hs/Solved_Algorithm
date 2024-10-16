import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
    int v,w,u;
    Edge(int v,int w,int u){
        this.v=v;
        this.w=w;
        this.u=u;
    }
    @Override
    public int compareTo(Edge e){
        return this.w-e.w;
    }
}

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());

        ArrayList<Edge>[] graph = new ArrayList[n + 1];
        for(int i=0;i<graph.length;i++){
            graph[i]=new ArrayList<Edge>();
        }
        for(int i=0;i<m;i++){
            st= new StringTokenizer(br.readLine());
            int u=Integer.parseInt(st.nextToken());
            int v=Integer.parseInt(st.nextToken());
            int w=Integer.parseInt(st.nextToken());
            graph[u].add(new Edge(v,w,u));
            graph[v].add(new Edge(u,w,v));
        }
        prim(graph, n);
    }
    public static void prim(ArrayList<Edge>[] graph,int n){
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        boolean[] visited = new boolean[n+1];
        int sum=0;
        for(Edge e:graph[1]){
            pq.add(e);
        }
        visited[1]=true;
        while(!pq.isEmpty()){
            Edge e = pq.poll();
            if(visited[e.v]) continue;
            visited[e.v]=true;
            sum+=e.w;
            for(Edge next:graph[e.v]){
                if(!visited[next.v]){
                    pq.add(next);
                }
            }
        }
        System.out.println(sum);
    }
}