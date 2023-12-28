import java.util.*;

class Solution {

    static int n, m, id;
    static boolean[][] visited;
    static int[][] oil; // 석유 덩어리의 ID 저장하는 배열
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    public int solution(int[][] land) {
        int answer = 0;
        n = land.length;
        m = land[0].length;
        visited = new boolean[n][m];
        int oilId = 0;                  // 석유 덩어리의 ID
        oil = new int[n][m];            // 석유 덩어리의 ID 저장하는 배열

        Map<Integer, Integer> oilSize = new HashMap<>();

        for(int j=0; j<m; j++) {
            for(int i=0; i<n; i++) {
                if(land[i][j] == 1 && !visited[i][j]) {
                    int temp = bfs(i,j,land,oilId);
                    oilSize.put(oilId, temp);
                    oilId++;
                }
            }
        }

        // 석유 덩어리의 ID를 저장한 배열과 Set 이용하여 연결된 석유 덩어리의 크기를 구함
        int[] oilSum = new int[m];
        for(int j=0; j<m; j++) {
            Set<Integer> oilSet = new HashSet<>();
            for(int i=0; i<n; i++) {
                if(land[i][j] == 1) {
                    oilSet.add(oil[i][j]);
                }
            }
            for(int id : oilSet) {
                oilSum[j] += oilSize.get(id);
            }
        }

        return Arrays.stream(oilSum).max().getAsInt();
    }

    public int bfs(int i, int j, int[][] land, int oilId) {
        int cnt = 1;
        visited[i][j] = true;
        oil[i][j] = oilId;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{i,j});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for(int k=0; k<4; k++) {
                int nx = cur[0] + dx[k];
                int ny = cur[1] + dy[k];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] || land[nx][ny] == 0) continue;
                if (land[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    oil[nx][ny] = oilId;
                    q.offer(new int[]{nx,ny});
                    cnt++;
                }
            }

        }
        return cnt;
    }
}
