import java.util.Scanner;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if(Math.abs(o1)==Math.abs(o2)){
                    return o1 - o2;
                }
                else{
                    return Math.abs(o1) - Math.abs(o2);
                }
            }
        });

        for(int  i = 0; i < n; i++){
            int  temp = sc.nextInt();
            if(temp == 0){
                int out = pq.isEmpty() ? 0 : pq.poll();
                System.out.println(out);
            }
            else{
                pq.offer(temp);
            }
        }
        
    }
}
