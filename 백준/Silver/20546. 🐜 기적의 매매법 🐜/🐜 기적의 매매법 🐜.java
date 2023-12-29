import java.util.*;
import java.io.*;

public class Main {

    static int junMoney, seongMoney;
    static int junTotalPrice = 0;
    static int seongTotalPrice = 0;
    static int junStock = 0;
    static int seongStock = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[14];
        junMoney = N;
        seongMoney = N;
        junStock = 0;
        seongStock = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 14; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        br.close();

        // 준현이 주식 구매
        for(int stockPrice: arr) {
            if(junMoney >= stockPrice) {
                junStock += (junMoney / stockPrice);
                junMoney %= stockPrice;
            }
        }

        // 준현이 총 금액
        junTotalPrice = junMoney + (junStock * arr[13]);

        /* 성민이 주식 구매
         * 1. 모든 거래는 전량 매수와 전량 매도
         * 2. 3일 연속 가격이 전날 대비 상승하면 다음날 무조건 가격 하락 가정 동일한 가격은 상승 x
         * 3. 3일 연속 가격이 전날 대비 하락하면 다음날 무조건 가격 상승 가정 동일하 가격은 하락 x
         * 즉, 매수 타이밍은 3일 연속 하락한 날 먼저 매수하고 팔아야함, 마지막까지 연속 상승이 없으면 마지막날 매도
         */
        int buy_stock = 0;
        int sell_stock = 0;
        for(int i=1; i < 14; i++) {

            // 값이 하락하는 경우
            if(arr[i] < arr[i-1]) {
                buy_stock ++;

                // 3일 이상 하락하는 경우(매수)
                if(buy_stock >= 3) {
                    seongStock += (seongMoney / arr[i]);
                    seongMoney %= arr[i];
                }
            } else {
                buy_stock = 0;
            }

            // 값이 상승하는 경우
            if(arr[i] > arr[i-1]) {
                sell_stock ++;

                // 3일 이상 상승하고 산 주식이 있는 경우(매도)
                if(sell_stock >= 3 && seongStock > 0) {
                    seongMoney += (seongStock * arr[i]);
                    seongStock = 0;
                }
            } else {
                sell_stock = 0;
            }
        }

        // 성민이 총 금액
        seongTotalPrice = seongMoney + (seongStock * arr[13]);

        // 결과 출력
        if(junTotalPrice > seongTotalPrice) {
            bw.write("BNP");
        } else if(junTotalPrice < seongTotalPrice) {
            bw.write("TIMING");
        } else {
            bw.write("SAMESAME");
        }

        bw.flush();
        bw.close();

    }
}