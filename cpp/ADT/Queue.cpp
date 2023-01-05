#include <iostream>
#include <string>
using namespace std;

#define MQS 100 // MAX_QUEUE_SIZE

class Queue { // Queue
protected:
    // front index가 가리키는 공간에는 값이 할당되지 않은 상태여야 함. (item이 없는 상태)
    int frontInd; // 첫번 째 item 하나 앞의 index
    int rearInd; // 마지막 item index
    int count;  // 큐의 현재 size를 나타냄
    string data[MQS]; // item 배열
public:
    // 공백상태(isEmpty)와 포화상태(full)를 구별하기 위해 하나의 공간(dummy)은 항상 비워둠.
    Queue() { // 초기화 
        count = 0;
        frontInd = rearInd = 0; 
    }
    bool full() { // 큐가 가득 차있으면 true
        return (rearInd + 1) % MQS == frontInd; // 포화상태
    }
    void enqueue(string val) { // 파라미터로 주어진 item을 rear에 추가
        if ( full() ) {
            cout << "Queue가 가득 찼습니다." << endl;
        }else {
            count++; // enqueue 이므로 큐에 item 추가 -> size 증가
            // 큐의 rear에 새로운 item 삽입
            rearInd= (rearInd +1) % MQS; // 원형 큐이므로 index를 넘지 않게 MQS로 나눈 나머지로 진행
            data[rearInd] = val; // 큐의 맨 뒤에 item 삽입
        }
    }
    string dequeue() { // 큐가 비어있지 않으면, 맨 앞 item을 삭제하고 반환
        if ( isEmpty() ) { // 
            cout << "큐가 비어있습니다." << endl;
        }else {
            count--; // dequeue 이므로 큐 size 감소
            // 감소이므로 맨 앞을 나타내는 front index 값을 증가시킴
            frontInd = (frontInd + 1) % MQS;
            return data[frontInd];
        }
    }
    bool isEmpty() { // 큐가 비어 있으면 true 반환
        return frontInd == rearInd; // 공백상태
    }
    int size() { // 큐의 모든 item 갯수 반환
        return count; // item 수 반환
    }
};

int main() {
    Queue que;
    
    int n; cin >> n; // 몇 번의 연산을 진행할 것인지를 나타냄.
    for(int i=0; i<n; i++) {
        string s; cin >> s;
        // 포맷 예시) enqueue 6
        if (s=="enqueue") { // adds a new item to the rear of the queue.
            string t; cin >> t;
            que.enqueue(t);
        }else if (s=="dequeue") { // removes the front item from the queue.
            cout << que.dequeue() << endl;
        }else if (s=="size") { // returns the number of items in the queue.
            cout << que.size()<<endl;
        }else if (s=="empty") { 
            if (que.isEmpty()) { // tests to see whether the queue is empty.
                cout << "큐가 비어 있음" << endl;
            }
            else {
                cout << "큐가 비어 있지 않음" << endl;
            }
        }
        else {
            cout << "다시 입력하세요." << endl;
        }
    }
    return 0;
}