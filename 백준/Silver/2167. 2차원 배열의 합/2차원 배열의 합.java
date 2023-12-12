import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];
        int[][] prefix_sum = new int[N+1][M+1];

        for(int i=0;i<N;i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<M;j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=1;i<=N;i++) {
            for(int j=1;j<=M;j++) {
                prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1];
            }
        }

        int K = Integer.parseInt(br.readLine());

        // 2차원 배열에서 구간합은 구하는 구간의 행-1 누적합과 열-1 누적합을 빼주고 중복으로 빼준 행-1,열-1 을 더해준다.
        for(int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int result = prefix_sum[x][y] - prefix_sum[x][b-1] - prefix_sum[a-1][y] + prefix_sum[a-1][b-1];
            System.out.println(result);
        }
    }

    /*
    TIL/회고
    - 코테에서 자주 보이는 누적합과 구건합 기본적으로 누적합에서 구간간의 차이를 빼주면 되지만 2차원 배열은 너무 낯설었다.
    - 기존 1차원 계산처럼 2,1은 1,1 + 1,2 + 1,3 + 2,1이 아닌 1,1 + 2,0 이다.
    - 1차원 배열의 누적합 처럼 2차원 배열의 누적합도 범위를 꼭 N+1, M+1으로 하자. 그래야 초기 값들이 0으로 누적합이 돼서 편하다.
    - 안 그러면 조건문으로 i나 j가 0보다 큰 경우 - [i-1][j-1], i가 0보다 큰 경우 + [i-1][j] 등의 조건이 필요하다.
     */
}