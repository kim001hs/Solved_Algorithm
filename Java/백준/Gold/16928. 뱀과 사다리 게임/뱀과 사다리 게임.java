import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    static int[] map = new int[101];

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 사다리 개수
        int m = sc.nextInt(); // 뱀의 개수

        // 기본적으로 각 칸은 자기 자신으로 설정
        for (int i = 1; i <= 100; i++) {
            map[i] = i;
        }

        // 사다리 입력 처리
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            map[x] = y; // x에서 y로 이동하는 사다리
        }

        // 뱀 입력 처리
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            map[u] = v; // u에서 v로 이동하는 뱀
        }

        // BFS 탐색 시작
        BFS();
    }

    public static void BFS() {
        boolean[] visited = new boolean[101];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{1, 0}); // {현재 위치, 이동 횟수}
        visited[1] = true;

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int current = temp[0];
            int move = temp[1];

            // 100번 칸에 도착하면 이동 횟수를 출력하고 종료
            if (current == 100) {
                System.out.println(move);
                return;
            }

            // 주사위는 1~6까지의 범위로 굴림
            for (int i = 1; i <= 6; i++) {
                int next = current + i;

                // 범위를 벗어나면 무시
                if (next > 100) continue;

                // 이동할 칸이 사다리나 뱀에 의해 변경된 경우 그 목적지로 이동
                next = map[next];

                // 아직 방문하지 않은 칸이면 큐에 추가
                if (!visited[next]) {
                    visited[next] = true;
                    q.add(new int[]{next, move + 1});
                }
            }
        }
    }
}
