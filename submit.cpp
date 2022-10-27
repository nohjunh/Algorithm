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
int visited[MAX_SIZE][MAX_SIZE] = { false };
int moveCount[MAX_SIZE][MAX_SIZE] = { 1 };

queue<pair<int, int>> q;
int M, N;

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0 , -1 };

bool IsInside(int moveY, int moveX) {
	return (0 <= moveX && 0 <= moveY && moveX < M&& moveY < N);
}

void bfs(pair<int,int> start) {
	int y = start.first;
	int x = start.second;
	q.push(make_pair(y, x));

	while (!q.empty()) {
		int y = q.front().first; // first가 y자표(배열이[][]일때 앞에것이 행이므로)
		int x = q.front().second;
		if (y == N-1 && x == M-1) { // 도착점에 왔다면,
			break; 
		}
		q.pop();

		for (int i = 0; i < 4; i++) {
			int moveY = y + dy[i];
			int moveX = x + dx[i];
			if (IsInside(moveY, moveX) == true && graph[moveY][moveX] == 1 &&
				visited[moveY][moveX]==false){ // 1이여야 갈 수 있음
				visited[moveY][moveX] = true; // 방문했음을 알려주려고 true으로 체크
				moveCount[moveY][moveX]= moveCount[y][x]+1;
				q.push(make_pair(moveY, moveX));
			}
		}
	}
}

int main() {
	cin >> N >> M;

	// N= 세로 칸의 수 ,M=가로 칸의 수
	/* 그래프 정보 입력*/
	for (int i = 0; i < N; i++) {
		string row;
		cin >> row; // 띄어쓰기없이 입력이 들어올 때
		for (int j = 0; j < M; j++) {
			graph[i][j] = row[j] - '0'; // string의 각 문자를 숫자로 바꿈
		}
	}

	bfs(make_pair(0, 0));

	cout << moveCount[N-1][M-1] << endl;

	return 0;
}