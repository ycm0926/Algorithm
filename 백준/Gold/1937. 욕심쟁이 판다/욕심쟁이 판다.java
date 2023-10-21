import java.io.*;
import java.util.*;

public class Main {

    static int N, ans;
    static int[][] graph, visited;
    static int[] dx = {0,0,-1,1}, dy = {1,-1,0,0};
    static Queue<Integer> q = new LinkedList<>();


    public static int dfs(int x, int y) {
        if (visited[x][y] == -1) {
            visited[x][y] = 1;

            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && graph[nx][ny] > graph[x][y]) {
                    visited[x][y] = Math.max(visited[x][y], dfs(nx, ny) + 1);
                }
            }
        }
        return visited[x][y];
    }


    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        graph = new int [N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new int [N][N];
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                visited[i][j] = -1;
            }
        }

        ans = 0;

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                ans = Math.max(ans, dfs(i, j));
            }
        }
        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();
        br.close();
    }
}