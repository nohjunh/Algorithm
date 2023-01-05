// 우선 순위 큐를 이용해
// 방문할 수 있는 정점 중 가중치가 가장 낮은 정점으로 이동
/*
/////////////////////////////
// 우선순위 큐를 <자료형, 구현체, 비교연산자> 를 이용하여 선언한다.
// 비교연산자에 greater<int>를 사용하여 int가 작은값이 우선한다.
priority_queue <int, vector<int>, greater<int> > pq;
//////////////////////////////////////////////
*/
#define _CRT_SECURE_NO_WARNINGS
#include<queue>
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

#define MAX_SIZE 10001

bool visit[MAX_SIZE] = { false };
vector<pair<int, int>> Edge[10001];

int prim() {

    int sum = 0;
    // 우선 순위 큐(최소 힙)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, 1)); // 1번 정점부터 시작 // 가중치=0

    while (!pq.empty()) {
        pair<int, int> current = pq.top();
        pq.pop();

        if (visit[current.second]) { // 방문 했었다면 판단할 필요 없으므로 그냥 넘김
            continue;
        }

        // prim은 visit 체크를 함으로써 사이클을 방지한다.
        visit[current.second] = true; // 방문처리 해줌.

        sum += current.first; // 가중치를 더해줌.

        // 각 Node와 연결되는 Edge 정보를 가지고 있는데,
        // 현재 Node에서 이동할 수 있는 방문하지 않은 Node를 Push !
        for (int i = 0; i < Edge[current.second].size(); i++) {
            if (visit[Edge[current.second][i].second] == false) { // Node정보가 나올 것이다. 만약 방문하지 않았다면,
                pq.push(Edge[current.second][i]); // pq에 넣게되면 알아서 최솟값이 root로 올라갈 것이다. 그래서 최솟값 선별이 가능해짐.
            }
        }
    }
    return sum;
}

int main() {
    int V, E;
    cin >> V >> E;

    for (int i = 0; i < E; i++) {
        int A, B, C;
        cin >> A >> B >> C;

        // push_back에 들어가는 pair의 first=가중치, second= 두번째 node
        Edge[A].push_back(make_pair(C, B));
        Edge[B].push_back(make_pair(C, A));
    }

    cout << prim() << endl;

    return 0;
}
