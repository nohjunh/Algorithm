#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <string>
#include <deque>
#include <queue>
#include <vector>
#include <sstream>

#define MAX_SIZE 1002
using namespace std;

int graph[MAX_SIZE][MAX_SIZE];
queue<pair<int, int>> q;
vector<pair<int, int>> one_list;
int M, N;

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0 , -1 };

bool IsInside(int moveY, int moveX) {
	return (0 <= moveX && 0 <= moveY && moveX < M && moveY < N);
}

void bfs(vector<pair<int,int>> one_list){
	for (int i = 0; i < one_list.size(); i++) {
		int y = one_list[i].first;
		int x = one_list[i].second;
		q.push(make_pair(y, x));
	}

	while (!q.empty()) {
		int y= q.front().first;
		int x= q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int moveY = y + dy[i];
			int moveX = x + dx[i];
			if (IsInside(moveY, moveX) == true && graph[moveY][moveX] == 0) {
				graph[moveY][moveX]= graph[y][x]+1;
				q.push(make_pair(moveY, moveX));
			}
		}
	}
}

int main() {
	cin >> M >> N;
	// M= 가로 칸의 수, N= 세로 칸의 수
	/* 그래프 정보 입력*/
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> graph[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (graph[i][j] == 1) {
				one_list.push_back(make_pair(i, j));
			}
		}
	}

	bfs(one_list);

	int max_day = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (graph[i][j] == 0) {
				cout << "-1" << endl;
				return 0;
			}
			else {
				max_day = max(graph[i][j], max_day);
			}
		}
	}

	// 1일차부터 시작했으므로 day로는 -1 빼줘야 됨.
	cout << max_day-1 <<endl;
	
	return 0;
}