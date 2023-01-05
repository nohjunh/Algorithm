#include <vector>
#include <iostream>
#include <queue>

#define MAX 1001 // 정점의 수 2<=N<=1000
#define INF 99999999
using namespace std;

int path[1001];

vector<int> dijkstra(int start, int N, vector<pair<int, int> > graph[]) {
    vector<int> dist(N + 1, INF);    // 전부 INF로 초기화 
    priority_queue<pair<int, int> > pq;

    dist[start] = 0;
    pq.push(make_pair(0, start));    // start정점 먼저 push, 즉 방문


    while (!pq.empty()) {
        int cost = -pq.top().first;    // 방문한 정점의 가중치
        int cur = pq.top().second;    // 현재 위치한 정점
        pq.pop();

        if (cost > dist[cur]) // 탐색할 필요가 없는 정점이라면 가지치기를 해준다.
            continue;

        for (int i = 0; i < graph[cur].size(); i++) {
            int next = graph[cur][i].first; // 탐색할 다음 정점
            int adjnextCost = cost + graph[cur][i].second;    // 현재 방문한 정점을 거쳐서 다음 정점을 갈때의 비용 
            if (adjnextCost < dist[next]) {
                dist[next] = adjnextCost;    // 최신화
                path[next] = cur; // 다음 노드로 가는 최단 경로를 나타내기 위해 현재 정점을 넣어줌 즉, A->B 노드가 최단경로일 때 B노드(next)로 가기 위해서는 A노드(cur)를 거쳐서 가야함
                pq.push(make_pair(-adjnextCost, next));
            }
        }
    }
    return dist;
}

int main()
{
    int N, M; // N개의 도시, M개의 버스
    vector<pair<int, int> > graph[MAX];
    cin >> N;
    cin >> M;

    for (int i = 0; i < M; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        graph[from].push_back(make_pair(to, cost));
    }

    int startCity, endCity;
    cin >> startCity >> endCity;

    vector<int> dist = dijkstra(startCity, N, graph);


    cout << dist[endCity] << endl; // 출발도시에서 도착도시까지 가는데 드는 최소비용

    // vector를 이용한 경로 역추적
    vector<int> path_vector;
    int temp = endCity;
    while (temp) {  // path[temp]의 값이 있다면, 즉 temp(next)노드로 가기 위해 그 전에 거치는 정점이 있다면 벡터에 넣어줌.
        // 반복하여 넣어주면 벡터에는 end정점~출발정점 순으로 저장되게 됨. 따라서 역순으로 다시 출력해주는 절차가 필요.
        path_vector.push_back(temp);
        temp = path[temp];
    }

    cout << path_vector.size() << endl; // 최소 비용을 갖는 경로에 포함되어있는 도시의 개수

    for (int i = path_vector.size() - 1; i >= 0; i--) {  // 역순으로 경로 출력
        cout << path_vector[i];
        if (i != 0) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}