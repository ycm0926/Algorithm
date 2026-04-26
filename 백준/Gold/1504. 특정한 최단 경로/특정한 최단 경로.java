import java.util.*;
import java.io.*;

/*
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.



4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

 */

public class Main {

    static ArrayList<Node>[] graph;
    static int nodeCnt, EdgeCnt;
    static int MAX_VALUE = 100000000;
    static int[] essential;

    static class Node implements Comparable<Node> {
        int to;
        int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return this.cost - o.cost;
        }

        @Override
        public String toString() {
            return "(to=" + to + ", cost=" + cost + ")";
        }
    }

    public static int[] dijkstra(int start) {
        boolean[] visited = new boolean[nodeCnt+1];
        int[] distance = new int[nodeCnt+1];
        Arrays.fill(distance, MAX_VALUE);
        distance[start] = 0;
        PriorityQueue<Node> q = new PriorityQueue<>();
        q.add(new Node(start, 0));

        while (!q.isEmpty()) {
            Node curNode = q.poll();

            // 방문 했다면? 그만
            if(visited[curNode.to])continue;
            visited[curNode.to] = true;

            for(int i = 0; i < graph[curNode.to].size(); i++) {
                Node next = graph[curNode.to].get(i);

                if(distance[next.to] > distance[curNode.to]+next.cost) {
                    distance[next.to] = distance[curNode.to]+next.cost;
                    q.add(new Node(next.to, distance[curNode.to]+next.cost));
                }
            }
        }

        return distance;
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        nodeCnt = Integer.parseInt(st.nextToken());
        EdgeCnt = Integer.parseInt(st.nextToken());
        graph = new ArrayList[nodeCnt+1];
        essential = new int[2];

        for(int i = 0; i <= nodeCnt; i++){
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < EdgeCnt; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph[from].add(new Node(to, cost));
            graph[to].add(new Node(from, cost));
        }

        st = new StringTokenizer(br.readLine());
        essential[0] = Integer.parseInt(st.nextToken());
        essential[1] = Integer.parseInt(st.nextToken());

        int[] distFrom1  = dijkstra(1);
        int[] distFromV1 = dijkstra(essential[0]);
        int[] distFromV2 = dijkstra(essential[1]);

        long path1 = (long)distFrom1[essential[0]] + distFromV1[essential[1]] + distFromV2[nodeCnt];
        long path2 = (long)distFrom1[essential[1]] + distFromV2[essential[0]] + distFromV1[nodeCnt];

        if(path1 < MAX_VALUE || path2 < MAX_VALUE) {
            System.out.println(Math.min(path1, path2));
        } else {
            System.out.println(-1);
        }
    }
}