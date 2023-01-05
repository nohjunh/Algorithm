#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <string>
#include <deque>
#include <queue>
#include <vector>
#include <sstream>
using namespace std;

int main() {
	deque<int> dq;
	int N, M;
	cin >> N >> M;
	int left = 0;
	int right= 0;
	int cnt = 0;

	for (int i = 1; i <= N; i++) {
		dq.push_back(i);
	}
	for (int i=0; i < M; i++) {
		int index;
		cin >> index;
		for (int i = 0; dq.size(); i++) {
			if (dq[i] == index) {
				left = i;
				right = dq.size() - i;
				break;
			}
		}
		if (left <= right) { // 왼쪽 원소를 오른쪽으로 이동시키는게 더 낫다
			while(1){
				if (dq.front() == index) {
					break;
				}
				dq.push_back(dq.front());
				dq.pop_front();
				cnt++;
			}
			dq.pop_front();
		}
		else { // left가 right보다 더 길기에 오른쪽 원소를 왼쪽으로 이동시키는게 더 낫다
			cnt++;
			while (1) {
				if (dq.back() == index) {
					break;
				}
				dq.push_front(dq.back());
				dq.pop_back();
				cnt++;
			}
			dq.pop_back();
		}
	}
	cout << cnt << endl;

	return 0;
}