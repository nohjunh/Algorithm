// 1260
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

bool visited[1002] = { false };
vector<int> a[10002];

void initial() {
	for (int i = 1; i <= 1001; i++) {
		visited[i] = false;
	}
}
void dfs(int start) {
	visited[start] = true;
	cout << start << " ";
	for (int i = 0; i < a[start].size(); i++) {
		int next = a[start][i];
		if (visited[next] == false) {
			dfs(next);
		}
	}
}

void bfs(int start) {
	queue<int> q;
	visited[start] = true;
	q.push(start);

	while (!q.empty()) {
		int now = q.front();
		q.pop();
		cout << now << " ";


		for (int i = 0; i < a[now].size(); i++) {
			int next = a[now][i];

			if (visited[next] == false) {
				visited[next] = true;
				q.push(next);
			}
		}
	}
}


int main() {
  	int N, M, V;
	cin >> N >> M >> V;

	for (int i = 0; i < M; i++) {
		int first, second;
		cin >> first >> second;
		a[first].push_back(second);
		a[second].push_back(first);
	}

	for (int i = 1; i <= N; i++) {
		sort(a[i].begin(), a[i].end());
	}

	dfs(V);
	cout << endl;

	initial();
	bfs(V);

	return 0;
}