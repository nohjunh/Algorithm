#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <string>
#include <deque>
#include <queue>
#include <sstream>
using namespace std;

int main() {
    queue<int> q;
    int N;
    cin >> N;
    
    for(int i=0; i<N; i++){
        q.push(i+1);
    }
    while(q.size()!=1){
        q.pop();
        int first= q.front();
        q.pop();
        q.push(first);
    }
    cout << q.front()<<endl;

    return 0;
}