import java.io.*;
import java.util.*;

public class Main {

    static int[][] board = new int[5][5];
    static int num;
    static int cnt;
    static int ans = 1;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 빙고판 입력
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 빙고 숫자 입력
        for (int k = 0; k < 5; k++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            // 빙고 숫자 체크
            for (int i = 0; i < 5; i++) {
                num = Integer.parseInt(st.nextToken());

                for (int j = 0; j < 5; j++) {
                    for (int l = 0; l < 5; l++) {
                        if (board[j][l] == num) board[j][l] = 0;
                    }

                }

                row();
                col();
                cross1();
                cross2();
                if (cnt >= 3) {
                    System.out.println(ans);
                    System.exit(0);
                }
                cnt = 0;
                ans++;
            }
        }
    }

    public static void row() {
        for (int i = 0; i < 5; i++) {
            int zeroCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == 0) zeroCnt++;
            }
            if (zeroCnt == 5) cnt++;
        }
    }

    public static void col() {
        for (int i = 0; i < 5; i++) {
            int zeroCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (board[j][i] == 0) zeroCnt++;
            }
            if (zeroCnt == 5) cnt++;
        }
    }

    public static void cross1() {
        int zeroCnt = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][i] == 0) zeroCnt++;
        }
        if (zeroCnt == 5) cnt++;
    }

    public static void cross2() {
        int zeroCnt = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][4 - i] == 0) zeroCnt++;
        }
        if (zeroCnt == 5) cnt++;
    }
}