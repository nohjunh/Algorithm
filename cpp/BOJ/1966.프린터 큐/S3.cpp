#include <iostream>
#include <queue>
using namespace std;

int main() {
	int TestCase;
	int N, M, value;
	int countPrint = 0;

	cin >> TestCase;

	for (int k = 0; k < TestCase; k++) {
		countPrint = 0;
		cin >> N >> M;
		queue<pair<int, int>> q;
		priority_queue<int> PQ;
		for (int i = 0; i < N; i++) {
			cin >> value;
			q.push(make_pair(i, value));
			PQ.push(value);
		}
		while (!q.empty()) {
			int index = q.front().first;
			int value = q.front().second;
			if (PQ.top() != value) {
				q.push(q.front());
				q.pop();
			}
			else {
				q.pop();
				PQ.pop();
				countPrint++; // 몇번 출력 됐는지를 나타내는 변수 +1
				if (index == M) {
					cout << countPrint << endl;
					break;
				}
			}
		}
	}
	return 0;
}