#include <iostream>
#include <string>
using namespace std;
#define MAX_LIST_SIZE 100 // MAX_LIST_SIZE

class List {
	int data[MAX_LIST_SIZE]; // 1차원 배열에 item들을 저장
	// Length 변수= 리스트 마지막 item의 index +1 => 리스트 item의 갯수==length 값
	int length; // 리스트 마지막 item 다음을 가리키게 함.
public:
	List() { length = 0; }

	void remove(int pos); // pos번째 item을 리스트에서 제거 -> 65줄
	bool search(int item) { // loop 돌면서 해당 item이 있으면 true 반환, 없으면 false 반환 
		for (int i = 0; i < length; i++) {
			if (data[i] == item) {
				return true;
			}
		}
		return false;
	}
	bool isEmpty() { // length는 리스트 item의 갯수를 나타내기에 0이면 empty상태
		return length == 0;
	}
	int size() { // length는 리스트 item의 갯수
		return length;
	}
	bool full() {
		return length == MAX_LIST_SIZE; // 리스트가 가득 찼을때
	}

	void append(int item) {
		if (full()) {
			cout << "list가 가득 찼습니다." << endl;
			return;
		}
		data[length] = item; // length는 리스트 마지막 item의 index+1 이므로 end of the list를 가리킴.
		length++; // item이 들어갔으므로 length 1만큼 증가.
	}
	void insert(int pos, int item); // 리스트의 pos번째에 item 추가 -> 48줄
	int pop() {
		int popValue = data[length - 1];
		length--;
		return popValue; // 리스트의 마지막 아이템을 반환한다.
	}
};

void List::insert(int pos, int item) {
	if (full()) {
		cout << "list가 가득 찼습니다." << endl;
		return;
	}
	if (pos < 0 || pos > length) {
		cout << "out-of-index" << endl;
		return;
	}
	// List는 빈틈없는 집합이기에 빈 index가 없도록 쉬프트 과정을 거친다.
	for (int i = length; i > pos; i--) { // i==pos가 되면 for문 종료 // i가 length부터 시작 -> 가장 마지막요소부터 한 칸씩 땡길 예정
		data[i] = data[i - 1]; // pos위치에 item을 넣기 위해 pos 위치를 제외하고 다 한칸씩 뒤로 땡긴다.
	}
	data[pos] = item; // pos 위치에 item 삽입
	length++; // item 하나 추가이므로 length + 1
}

void List::remove(int item) {
	if (isEmpty()) {
		cout << "list가 비어있습니다." << endl;
		return;
	}
	if (!search(item)) {
		cout << "list에 해당 item이 없습니다." << endl;
		return;
	}
	for (int i = 0; i < length; i++) {
		if (data[i] == item) {
			// List는 빈틈없는 집합이기에 빈 index가 없도록 쉬프트 과정을 거친다.
			for (int j = i+1; i < length; i++) { // i==pos가 되면 for문 종료
				data[j-1] = data[j]; // 삭제된 index를 메꾸기 위해 한 칸씩 땡기는 과정이 들어감.
			}
			length--; // item 하나 삭제이므로 length - 1
		}
	}
}

int main() {
	List list;
	
	// adds a new item to the end of the list making it the last item in the collection.
	list.append(1);
	list.append(2);
	
	// adds a new item to the list at position pos.
	list.insert(0, 3);
	
	// returns the number of items in the list.
	cout << "Size : " << list.size() << endl;

	// searches for the item in the list.
	if (list.search(1)) {
		cout << "item이 list에 존재합니다." << endl;
	}
	else {
		cout << "item이 list에 존재하지 않습니다." << endl;
	}

	// removes the item from the list.
	list.remove(1);
	
	// searches for the item in the list.
	if ( list.search(1) ) {
		cout << "item이 list에 존재합니다." << endl;
	}
	else {
		cout << "item이 list에 존재하지 않습니다." << endl;
	}

	// removes and returns the last item in the list.
	cout << "pop() : " << list.pop() << endl;

	// tests to see whether the list is empty.
	if (list.isEmpty()) {
		cout << "list가 비어 있습니다." << endl;
	}
	else {
		cout << "list가 비어있지 않습니다." << endl;
	}

	return 0;
}