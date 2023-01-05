#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <string>
#include <deque>
#include <queue>
#include <sstream>
using namespace std;

int main() {
    deque<pair<int, int>> dq;
    int N;
    cin >> N;
    int now = 0;
    for (int i = 1; i <= N; i++) {
        int value;
        cin >> value;
        dq.push_back(make_pair(i, value));
    }

    while (!dq.empty()) {
        int value = dq.front().second;
        cout << dq.front().first << " ";
        dq.pop_front();

        if (value > 0) {
            for (int i = 0; i < value - 1; i++) {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        if (value < 0) {
            for (int i = 0; i > value; i--) {
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    return 0;
}