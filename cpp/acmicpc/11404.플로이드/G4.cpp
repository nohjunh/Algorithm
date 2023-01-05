#include <iostream>
#include <string>
#include <vector>

using namespace std;
#define MAX 101 // 2<=n<=100 개의 도시
#define INF 100000000

void solve() {
    int n, m; // n=도시(정점), m=버스(간선)
   // a->b 도시로 가는 cost를 2차원 배열에 적어준다. 각 행열 index가 a->b로 가는 것을 알려주고 그 위치에 저장된 값이 cost
    int graph[MAX][MAX];
    cin >> n;
    cin >> m;

    // 2차원 배열 table 초기화
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) {
                graph[i][j] = 0;
            }
            else {
                graph[i][j] = INF;
            }
        }
    }
    // 2차원 배열 출발도시 -> 도착도시 cost값 설정
    for (int i = 0; i < m; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        graph[from][to] = min(graph[from][to], cost);  // 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있기에 이런 식으로 표현
    }
    // 플로이드 와샬 GoGo
    // k= 거쳐가는 노드
    for (int k = 1; k <= n; k++) {
        // i= 출발노드
        for (int i = 1; i <= n; i++) {
            // j= 도착노드
            for (int j = 1; j <= n; j++) {
                if (graph[i][k] + graph[k][j] < graph[i][j]) {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }

    // 결과 출력
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] == INF) { // i에서 j로 갈 수 없는 경우에는 그 자리에 0 출력
                cout << 0 << " ";
                continue;
            }
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}