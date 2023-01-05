// #1655 가운데를 말해요
// 아이디어 참고: https://www.crocus.co.kr/625

// 중간값(가운데값) 구하기 알고리즘
// 1. 최대 힙의 크기는 최소 힙의 크기와 같거나, 하나 더 크다.
// 2. 최대 힙의 최대 원소는 최소 힙의 최소 원소보다 작거나 같다.
//	  이때 조건에 맞지 않다면 최대 힙, 최소 힙의 root값을 swap 해준다.
// ** 위 1,2번 규칙을 모두 만족하도록 유지한다면 항상 최대 힙 root값이 중간값이 됨.

#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	// 동적으로 요소가 들어오더라도 그 요소의 order를 유지시키기 위해선
	// Priority_queue를 사용한다.

	priority_queue<int> max_heap; // Max_Heap
	priority_queue<int, vector<int>, greater<int>> min_heap; // Min_Heap
	int N;
	cin >> N; // 외치는 정수의 갯수

	for (int s = 0; s < N; s++) {
		int input;
		cin >> input;

		if (max_heap.size() == min_heap.size()){
			max_heap.push(input);
		}
		else {  // 같지않다면, max_heap이 min_heap보다 하나 더 많은 상태이므로,
			min_heap.push(input);  // min_heap에 넣어줘서 1번 조건을 맞춰준다.
		}
		// 2번 조건에 맞지 않다면, 즉 최대힙의 root가 최소힙의 root보다 크다면
		if (!max_heap.empty() && !min_heap.empty()) {
			if (max_heap.top() > min_heap.top()) {
				// swap을 진행
				int max_value, min_value;
				max_value = max_heap.top();
				min_value = min_heap.top();
				max_heap.pop();
				min_heap.pop();
				max_heap.push(min_value);
				min_heap.push(max_value);
			}
		}
		cout << max_heap.top() << "\n"; // max_heap의 root가 중간값이 된다.
	}

	return 0;
}