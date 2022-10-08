// 2346 풍선터뜨리기 (cpp)
#include <iostream>
#include <string>
#include <deque>
#include <math.h>
using namespace std;

int main() {
    deque<pair<int,int>> q;
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        int num;
        cin >> num;
        q.push_back({ i,num });
    }

    while(q.size()!=0){
        int popRange = q.front().second;
        cout << q.front().first << " "; // 해당 index번호 출력
        q.erase(q.begin()); // 해당 풍선 터뜨리기
        if (q.size() == 0) {
            break;
        }
        if(popRange >= 1) { // 양수라면
            for (int j = 0; j < popRange - 1; j++) {
                q.push_back(q.front());
                q.erase(q.begin());
            }
        }
        else { // 음수라면
            for (int j = 0; j < abs(popRange); j++) {
                q.push_front(q.back());
                q.pop_back();
            }
        }
    }
    cout << endl;
    return 0;
}