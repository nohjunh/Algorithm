#include <iostream>
#include <string>
using namespace std;

const int MAX_STACK_SIZE=100; // 스택의 최대 크기 설정
class Stack {
private:
    string data[MAX_STACK_SIZE]; // 요소 배열
    int max_len; // 스택의 빈 공간 사이즈
    int top_ptr; // 스택 상단을 가리키는 변수

public:
    Stack(){ // 스택 생성자
        max_len= MAX_STACK_SIZE-1;
        top_ptr= -1; // top은 -1로 초기화 (index 0부터 요소가 들어가기 때문)
    }
    ~Stack(){ // 스택 소멸자
    }
    void push(string str) { // 스택의 top에 item 삽입
        if(top_ptr == max_len) {  // 꽉 차 있다면 
            cout<< "stack is full";
        }else{
            data[++top_ptr] = str; // top을 1 증가 시키고 그 곳에 item 삽입
        }
    }
    string pop() { // 스택의 top item을 삭제.
        if(top_ptr == -1) { // 스택이 비어있다면
            return "empty";
        }else{ 
            return data[top_ptr--]; // top item을 반환하고 top index 내려줌.
        }
    }
    string peek() { // 삭제하지 않고 top item 반환
        if (top_ptr == -1) { //
            return "empty";
        }
        else {
            return data[top_ptr];
        }
    }
    bool isEmpty() { // 비어있는지 확인
        return (top_ptr == -1);
    }
    int size() { // 스택에 들어있는 item 수 반환
        return top_ptr + 1; // index는 0부터 시작이므로 top이 가리키는 값 +1이 스택요소 size
    }
};

int main() {
    Stack stk;

    int n; cin >> n; // 몇 번의 연산을 진행할 것인지를 나타냄.
    for(int i=0; i<n; i++) {
    // 포맷 예시) push 1
     string s; cin >> s;
 
     if (s=="push") { // adds a new item to the top of the stack.
         string t; cin >> t;
         stk.push(t);
     }else if (s=="pop") { // removes the top item from the stack. 
         cout << stk.pop() << endl;
     }else if (s=="size") { // returns the number of items on the stack.
         cout << stk.size()<<endl;
     }else if (s=="empty") {  
         if (stk.isEmpty()) { // tests to see whether the stack is empty. returns boolean value
             cout << "스택이 비어 있음" << endl;
         }
         else {
             cout << "스택이 비어 있지 않음" << endl;
         }
     }else if (s=="peek") { // returns the top item from the stack but does not remove it.
         cout<< stk.peek()<<endl;
     }
     else {
         cout << "다시 입력하세요." << endl;
     }
    }
    return 0;
}