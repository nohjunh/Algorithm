// #1715 카드 정렬하기 (우선순위 큐, 그리디)
#include <iostream>
#include <queue>
using namespace std;

int main() {
	int N;
	priority_queue<int, vector<int>, greater<int>> min_heap; // Min_Heap
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		int input;
		cin >> input;
		min_heap.push(input);
	}
	
	int a, b, all = 0;
	while (min_heap.size() != 1) {
		a = min_heap.top(); min_heap.pop();
		b = min_heap.top(); min_heap.pop();
		min_heap.push(a + b);
		all += (a + b);
	}
	cout << all << "\n";

	return 0;
}