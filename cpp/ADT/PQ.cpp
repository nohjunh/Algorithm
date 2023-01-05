#include <iostream>
#include <string>
using namespace std;

#define MAX_HEAP_SIZE 200

class HeapNode {
private:
	int key; // key 값
public:
	HeapNode(int k = 0) : key(k){}
	void setKey(int k) {
		key = k;
	}
	int getKey() {
		return key;
	}
	void display() {
		printf("%4d", key);
	}
};

class MinHeap {
private:
	static const int root_index = 1;
	HeapNode node[MAX_HEAP_SIZE]; // item 배열
	int cur_size; // 힙의 현재 item의 갯수
public:
	MinHeap() : cur_size(0) { }
	bool isEmpty() {
		return this->cur_size == 0;
	}
	bool isFull() {
		return this->cur_size == MAX_HEAP_SIZE - 1;
	}

	HeapNode& getParent(int i) {  // 부모 노드
		return node[i / 2];
	}

	HeapNode& getLeft(int i) { // 왼쪽 자식 노드
		return node[i * 2];
	}

	HeapNode& getRight(int i) { // 오른쪽 자식 노드
		return node[i * 2 + 1];
	}

	HeapNode min() { // root_index에 있는 item이 가장 작은 값
		if (isEmpty()) {
			cout << "힙이 비어 있습니다." << endl;
		}
		else {
			return node[root_index];
		}
	}

	// 힙에 키 값 key를 갖는 새로운 item을 삽입
	void insert(int key) { 
		if (isFull()) { // 힙이 가득 찬 경우
			cout << "힙이 가득 찼습니다." << endl;
			return;
		}
		int i= ++cur_size; // 증가된 힙 크기 위치에서 시작
		
		// 트리를 거슬러 올라가면서 부모 노드와 비교하는 과정
		node[i] = key; // 트리의 맨 마지막에 해당 key 삽입하고 진행 -> 완전이진트리 형태 유지

		up_heap(i);
	}

	void up_heap(int i) {
		// i가 루트가 아니면서, 부모 노드보다 키 값이 작으면
		if (i != root_index && node[i].getKey() < getParent(i).getKey()) {
			swap(node[i], getParent(i));
			up_heap(i/2);
		}
	}

	HeapNode removeMin() {
		if (isEmpty()) {
			cout << "힙이 비어 있습니다." << endl;
			return NULL;
		}
		HeapNode item = node[root_index]; // 루트노드 (꺼낼 요소)
		node[root_index] = node[cur_size--]; // 마지막 노드를 root로 보냄
		down_heap(root_index); // heap-order를 맞추기 위해 루트부터 down_heap 진행
		return item; // 미리 저장해놓은 루트 값 반환
	}
	
	void down_heap(int i) {
      // 왼쪽 자식 노드에 관한 정보
		HeapNode left_child = getLeft(i);
		int left = i * 2;
      // 오른쪽 자식 노드에 관한 정보
		HeapNode right_child = getRight(i);
		int right = i * 2 + 1;

		int smallest = i;
      // smallest값과 바꾸기 위해선 자식 노드 중 더 작은 값을 찾아야 함.
		if (left <= cur_size && left_child.getKey() < node[smallest].getKey()) {
			smallest = left;
		}
		if (right <= cur_size && right_child.getKey() < node[smallest].getKey()) {
			smallest = right;
		}
		if (smallest != i) { // 값이 바뀌었다면, -> heap-order에 맞게 바꿔야 될 필요가 있다면
			swap(node[i], node[smallest]);
			down_heap(smallest);
		}
	}


	int size() { // 현재 PQ에 담긴 item 갯수 반환
		return cur_size;
	}

	void display() { // Heap 출력
		int count = 1; // count가 1->3->7->15 될 때마다 한 줄씩 띄우면 됨.
		for (int i = 1; i <= cur_size; i++) {
			node[i].display();
			if (i != cur_size && i == count) { // i번째가 count랑 같다면 한 줄 띄울 타이밍
				cout << endl;			   // i가 size랑 같다면 끝이므로 띄울 필요 X
				count = count*2+1;
			}
		}
		cout << endl;
		cout << "-----------------------" << endl;
	}
};

int main() {
	MinHeap heap;

	// inserts an entry with key k and value x.
	heap.insert(10);
	heap.insert(5);
	heap.insert(30);
	heap.insert(8);
	heap.insert(9);
	heap.insert(3);
	heap.insert(7);
	heap.display(); // 상태
	cout << "-------------" << endl;
	heap.min().display(); // return, but does not remove, an entry with smallest Key
	cout << " " << heap.size() << " "; // returns the number of items in the queue.
	cout << endl;
	cout << "-------------" << endl;
	// removes and returns the element with smallest Key.
	heap.removeMin();
	heap.display();
	cout << "-------------" << endl;
	heap.min().display(); // return, but does not remove, an entry with smallest Key
	cout << " " << heap.size() << " ";  // returns the number of items in the queue.
	cout << endl;
	cout << "-------------" << endl;
	heap.removeMin();
	heap.display();
	cout << "-------------" << endl;
	heap.min().display();
	cout << " " << heap.size() << " ";
	cout << endl;
	cout << "-------------" << endl;
	if (heap.isEmpty()) { // tests to see whether the queue is empty.
		cout << "Priority Queue가 비어 있습니다." << endl;
	}
	else {
		cout << "Priority Queue가 비어있지 않습니다." << endl;
	}
	cout << heap.size() << endl; // returns the number of items in the queue.
	cout << endl;

	return 0;
}