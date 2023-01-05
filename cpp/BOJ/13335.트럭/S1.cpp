#include <iostream>
#include <queue>
using namespace std;

int main() {
	int n, w, L;
	vector<int> trunk;
	queue<int> q;
	cin >> n >> w >> L;

	for (int i = 0; i < n; i++) {
		int weight;
		cin >> weight;
		trunk.push_back(weight);
	}
	int time = 0;
	int weight_sum = 0;
	for(int i=0; i<n; i++){
		while (1) {
			if (q.size() == w) {
				weight_sum -= q.front(); // 맨 앞에 트럭 제거
				q.pop();
			}
			if (weight_sum + trunk[i] <= L) {
				break;
			}
			q.push(0); // 무게가 L을 넘는 경우
			time++;
		}
		// q.size()도 자리가 있고 무게도 안넘을 때 트럭추가
		q.push(trunk[i]); 
		weight_sum += trunk[i];
		time++;
	}
	cout << time + w << endl;
	return 0;
}