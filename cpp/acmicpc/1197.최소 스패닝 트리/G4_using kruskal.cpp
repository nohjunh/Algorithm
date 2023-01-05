#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int check[10001];

class Edge {
public:
    int node[2]; // node[0]은 A노드, node[1]은 B노드를 가리킴
    int distance; // 가중치
    Edge(int a, int b, int distance) {
        this->node[0] = a;
        this->node[1] = b;
        this->distance = distance;
    }

    // edge를 오름차순으로 정렬할 때 기준을 distance로 정함.
    bool operator < (Edge& edge) {
        return this->distance < edge.distance;
    }
};

int getParent(int node) { // 노드의 parent 집합 구하기.
    if (check[node] == node) { // 해당 집합 component 번호 리턴
        return node;
    }
    return getParent(check[node]); // 해당 component의 root의 번호를 찾을 때 까지 올라감.
}

// 두 노드를 작은 값을 가지는 component 기준으로 연결한다.
void Union(int node1, int node2) {
    node1 = getParent(node1);
    node2 = getParent(node2);
    if (node1 < node2) {
        check[node2] = node1;
    }
    else {
        check[node1] = node2;
    }
}

// 사이클이 존재하면 true, 아니면 false 반환
bool isCycle(int node1, int node2) {
    node1 = getParent(node1);
    node2 = getParent(node2);
    if (node1 == node2) { // node1과 node2가 같은 component에 있는데
                            // 연결하게 되면 사이클이 생성되는 원리
        return true; // 사이클이 존재
    }
    else {
        return false;
    }
}


int main() {
    // 두 노드를 연결할 간선을 정함.
    vector<Edge> v;
    int V, E; // 정점의 수, 간선의 수
    cin >> V >> E;

    int A, B, C;
    for (int i = 0; i < E; i++) {
        cin >> A >> B >> C;
        v.push_back(Edge(A, B, C));
    }

    // 간선을 오름차순으로 정렬
    // 간선의 가중치가 작은 값부터 차례로 사이클 조사해가면서 tree를 연결해줄 것이다.
    sort(v.begin(), v.end());

    // check값을 각 노드 index로 초기화= 자기자신이 자기자신의 component번호
    for (int i = 1; i <= V; i++) {
        check[i] = i;
    }

    int sum = 0; // Minimum Spanning tree 총 비용
    for (int i = 0; i < v.size(); i++) {
        // 사이클이 존재하지 않으면 해당 간선을 연결하고 가중치를 더함.
        if (!isCycle(v[i].node[0], v[i].node[1])) { // 사이클이 아니라면
            sum += v[i].distance;
            Union(v[i].node[0], v[i].node[1]); // 두 노드가 연결 됐으므로
                                                    // 같은 component에 속하게 함.
        }
    }

    cout << sum <<endl;
    return 0;
}