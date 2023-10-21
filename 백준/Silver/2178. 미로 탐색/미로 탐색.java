import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;

    static int[][] graph, v;
    static int[] dx = {0, 0, -1, 1}, dy = {-1, 1, 0, 0};

    static Queue<Integer> q = new LinkedList<>();

    public static int bfs(int x, int y) {
        q.offer(x);
        q.offer(y);

        while(!q.isEmpty()) {
            x = q.poll();
            y = q.poll();

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];


                if(0 <= nx && nx < N && 0 <= ny && ny < M && graph[nx][ny] == 1) {
                    graph[nx][ny] = graph[x][y] + 1;
                    q.offer(nx);
                    q.offer(ny);
                }
            }

        }

        return graph[N-1][M-1];

    }

    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 그래프 입력
        graph = new int[N][M];
        for(int i=0; i <N; i++) {
            String s = br.readLine();

            for(int j=0; j<M; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }

        }

        // bfs 탐색
        bw.write(String.valueOf(bfs(0, 0)));
        bw.flush();
        bw.close();
    }
}