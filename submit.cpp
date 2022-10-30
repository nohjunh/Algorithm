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
	stack<int> s;
	vector<char> v;
	int n;
	cin >> n;
	int cur = 1;

	for (int i = 0; i < n; i++) {
		int input;
		cin >> input;

		while (cur <= input) { // input값까지 오름차순으로 받음.
			s.push(cur); // 오름차순으로 들어가야하기에 오름차순으로 넣어줌.
			v.push_back('+');
			cur++;
		}
		if (s.top() == input) { // input값에 해당하면 pop시킴.
			s.pop();
			v.push_back('-');
		}
		else { // top이 input가 같지 않다면 불가능한 것.
			cout << "NO" << "\n";
			return 0;
		}
	}

	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << "\n";
	}

	return 0;
}