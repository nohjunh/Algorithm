#include <iostream>
#include <string>
using namespace std;
#define MAX_INDICES_SIZE 100

// Implement HashTable using separate chaining
class Node {
public:
	int key;
	int value;
	Node* nextNode; // 충돌에 대해 자신의 다음 노드를 가르키기 위함.
	Node(int key, int value) {
		this->key = key;
		this->value = value;
		this->nextNode = nullptr;
	}
};

class HashTable {
private:
	Node** bucket; // bucket 포인터 배열을 가리키는 double pointer
public:
	HashTable() {
		bucket = new Node*[MAX_INDICES_SIZE];
		for (int i = 0; i < MAX_INDICES_SIZE; i++) {
			bucket[i] = nullptr; // 우선 nullptr로 초기화
		}
	}
	int hashFunc(int key) { // hash함수는 간단하게 Bucket의 최대 사이즈로 나눈 값을 활용한다.
		return key % MAX_INDICES_SIZE;
	}
	void put(int key, int value) {
		int hashcode = hashFunc(key);
		if (bucket[hashcode] == nullptr) { // 해당 버킷index가 비어있다면, 
			bucket[hashcode] = new Node(key, value); // 바로 연결시킴.
		}
		else {
			Node* curLinkNode = bucket[hashcode];
			while (curLinkNode->nextNode != nullptr && curLinkNode->key != key) { // 해당 bucket index에 연결된 노드가 더이상 없다면,
				curLinkNode = curLinkNode->nextNode; // linkNode의 주소를 해당 bucket index의 마지막 노드를 가리키게 하고
			}
			if (curLinkNode->key == key) { // 같은 key값을 갖는다면,
				curLinkNode->value = value; // 해당 key값에 대한 value를 최신화(replace)
			}
			else { // 같은 key 값을 가지는게 아니라면
				curLinkNode->nextNode = new Node(key, value);
			}
		}
	}
	int get(int key) {
		int hashcode = hashFunc(key);
		if (bucket[hashcode] == nullptr) { // 해당 버킷index가 비어있다면, 
			return -1;
		}
		else { // 해당 버킷 index에 linked Node가 존재한다면 
			Node* curLinkNode = bucket[hashcode];
			while (curLinkNode != nullptr && curLinkNode->key != key) { // 해당 bucket index에 연결된 노드가 더 있고 key값을 찾지 못했다면,
				curLinkNode = curLinkNode->nextNode; // linkNode의 주소를 다음번 노드를 가리키게 함.
			}
			if(curLinkNode == nullptr) { // 같은 key를 가지는 Node를 발견 못했다면,
				return -1;
			}
			else { // key를 찾았다면  
				return curLinkNode->value; // value 리턴
			}
		}
	}
	bool containsKey(int key) {
		int hashcode = hashFunc(key);
		if (bucket[hashcode] == nullptr) { // 해당 버킷index가 비어있다면, 
			return false;
		}
		else { // 해당 버킷 index에 linked Node가 존재한다면 
			Node* curLinkNode = bucket[hashcode];
			while (curLinkNode != nullptr && curLinkNode->key != key) { // 해당 bucket index에 연결된 노드가 더 있고 key값을 찾지 못했다면,
				curLinkNode = curLinkNode->nextNode; // linkNode의 주소를 다음번 노드를 가리키게 함.
			}
			if(curLinkNode == nullptr){ // 같은 key를 가지는 Node를 발견 못했다면,
				return false;
			}
			else { // 키를 찾았다면,
				return true;
			}
		}
	}

	bool contains(int value) { 
		for(int i=0; i<MAX_INDICES_SIZE; i++) { // value를 찾기 위해 bucket index별로 순서대로 확인
			Node* curLinkNode = bucket[i];
			while (curLinkNode != nullptr && curLinkNode->value != value) { // nullptr이 아니고 value를 찾지 못했다면,
				curLinkNode = curLinkNode->nextNode; // 연결된 다음 node를 가리킴.
			}
			if (curLinkNode != nullptr && curLinkNode->value == value) { // value를 찾았다면
				return true;
			}
		}
		return false;
	}

	void remove(int key) {
		int hashcode = hashFunc(key);
		if (bucket[hashcode] != nullptr) { // 해당 bucket index에 연결된 노드가 있다면,
			Node* curLinkNode = bucket[hashcode];
			Node* preLinkNode = nullptr;
			while (curLinkNode->nextNode != nullptr && curLinkNode->key != key) { // 다음 노드가 존재하고 현재 노드가 key가 아니라면,
				preLinkNode = curLinkNode; // 이전 노드는 현재 노드가 되고
				curLinkNode = curLinkNode->nextNode; // 현재 노드는 다음 노드가 됨.
			}
			if (curLinkNode->key == key) { // while문을 벗어난 이유가 key를 찾은거라면
				if (preLinkNode == nullptr) { // key가 해당 bucket index의 맨 처음에 있다면,
					Node* next = curLinkNode->nextNode; // 삭제할 노드의 다음 노드를 temp해놓고
					delete curLinkNode; // 삭제시킴.
					bucket[hashcode] = next; // 해당 bucket index의 처음은 삭제된 노드의 다음 노드가 된다.
				}
				else { // key가 해당 bucket index의 맨 처음이 아니라서 preLinkNode가 존재한다면,
					Node* next = curLinkNode->nextNode; // 삭제할 노드의 다음 노드를 temp해놓고
					delete curLinkNode; // 삭제시킴
					preLinkNode->nextNode = next; // 삭제한 노드의 이전 노드와 삭제한 노드의 다음을 연결시킴.
				}
			}
			else { // while문을 벗어난 이유가 Key값을 찾지 못한 거라면 그대로 끝
				return;
			}
		}
	}

};

int main() {
	HashTable hashTable;

	// the pair is inserted in the hash table if Key is a valid Key. if there was another value associated with this Key before,
	// it is replaced by the new value.
	hashTable.put(103, 10); // key=103, value=10인 노드 put
	hashTable.put(102, 9); // key=102, value=8인 노드 put
	hashTable.put(101, 8); // key=101, value=8인 노드 put
	hashTable.put(3, 5); // key=3, value=5인 노드 put
	hashTable.put(2, 6); // key=2, value=6인 노드 put
	hashTable.put(1, 7); // key=1, value=7인 노드 put

	// return value for Key if pair(key,value) is in the table.
	cout << hashTable.get(3) << endl;
	cout << hashTable.get(101) << endl;

	// returns true or false depending on whether there is an item with this key
	// in the table if key is valid.
	if (hashTable.containsKey(3)) {
		cout << "해당 Key를 가진 item이 존재합니다." << endl;
	}
	else {
		cout << "해당 Key를 가진 item이 존재하지 않습니다." << endl;
	}

	// returns true or false depending on whether there is such a value in the table.
	if (hashTable.contains(5)) {
		cout << "해당 value를 가진 item이 존재합니다." << endl;
	}
	else {
		cout << "해당 value를 가진 item이 존재하지 않습니다." << endl;
	}

	// removes item with the specified key if Key is valid.
	hashTable.remove(3);
	if (hashTable.get(3) == -1) {
		cout << "pair(key,value)가 존재하지 않습니다." << endl;
	}
	if (hashTable.containsKey(3)) {
		cout << "해당 Key를 가진 item이 존재합니다." << endl;
	}
	else {
		cout << "해당 Key를 가진 item이 존재하지 않습니다." << endl;
	}
	if (hashTable.contains(5)) {
		cout << "해당 value를 가진 item이 존재합니다." << endl;
	}
	else {
		cout << "해당 value를 가진 item이 존재하지 않습니다." << endl;
	}
	return 0;
}