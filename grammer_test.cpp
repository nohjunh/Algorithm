#include <iostream>
#include <string>
using namespace std;

#define MAX_GRAPH_SIZE 100

class Node {
private:
	int key; // key 값
public:
	Node(int k = 0) : key(k){}
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

class Edge {
private:
	Node v;
	Node w;
	double weight;
public:
	Edge(Node v, Node w, double weight=1) {
		this->v = v;
		this->w = w;
		this->weight = weight;
	}
	Node getFromVert() {
		return v;
	}
	Node getToVert() {
		return w;
	}
};

class Graph {
private:
	double adj[MAX_GRAPH_SIZE][MAX_GRAPH_SIZE] = { 0, }; // 인접행렬 ( 간선의 가중치를 저장하는 경우 1 대신 weight 저장)
	Node keys[MAX_GRAPH_SIZE]; // Key값 저장
	int indices[MAX_GRAPH_SIZE] = { 0, }; // key값을 넣으면 index를 반환해주는 배열
	int vertexindex; // 그래프에 vertex가 들어갈 index
public:
	Graph() : vertexindex(1) { } // index 0은 dummy

	void addVertex(Node vert) { // key vert를 가지는 노드 삽입
		indices[vert.getKey()] = vertexindex; // key를 넣으면 index를 반환함.
		keys[vertexindex] = vert; // 해당 index에 key값을 넣음
		vertexindex++; // index 증가
	}

	void addEdge(Node fromVert, Node toVert) {
		int fromVert_index = indices[fromVert.getKey()]; // 출발정점의 key가 있는 곳의 index
		int toVert_index = indices[toVert.getKey()]; // 도착정점의 key가 있는 곳의 index
		adj[fromVert_index][toVert_index] = 1; // 가중치가 안주어지면 1로 고정
	}

	void addEdge(Node fromVert, Node toVert, double weight) {
		int fromVert_index = indices[fromVert.getKey()];
		int toVert_index = indices[toVert.getKey()];
		adj[fromVert_index][toVert_index] = weight;
	}

	Node getVertex(int vertKey) { // key값을 받으면 해당 key값을 가지는 Node객체를 반환함.
		if (indices[vertKey] != 0) {   // 0이 아니라면 해당 key값을 가지는 Node객체가 있다는 뜻.
			int index = indices[vertKey];
			cout << "해당 Key값을 가지는 노드가 존재합니다." << endl;
			return keys[index];
		}
		else {
			cout << "해당 Key값을 가지는 노드가 존재하지 않습니다." << endl;
		}
	}
	
	Node* getVertices() {
		// list를 동적할당하여 keys에 들어있는 노드 수 만큼 받은 뒤 리턴함.
		Node* list = new Node[vertexindex];
		for (int i = 1; i <= vertexindex; i++) {
			list[i-1] = keys[i]; // keys의 index는 1부터 시작이지만, 반환할 list의 index는 0부터 시작해야 맞음.
		}
		return list;
	}

	bool hasVert(Node vert) {
		if (indices[vert.getKey()] != 0) {  // 0이 아니라면 해당 key값을 가지는 Node객체가 있다는 뜻.
			return true;
		}
		else {
			return false;
		}
	}

	bool hasEdge(Edge e) {
		int fromVert_index = indices[e.getFromVert().getKey()];
		int toVert_index = indices[e.getToVert().getKey()];
		if (adj[fromVert_index][toVert_index] != 0) { // 0이 아니라면 Edge가 존재한다는 뜻!
			return true;
		}
		else {
			return false;
		}
	}
};

int main() {
	Graph graph;

	// Adds an instance of Vertex to the graph
	graph.addVertex(Node(2)); // key 2를 갖는 vertex 추가 -> index 1에 저장
	graph.addVertex(Node(3)); // key 3을 갖는 vertex 추가 -> index 2에 저장
	graph.addVertex(Node(1));
	graph.addVertex(Node(5));
	
	// Adds a new, directed edge to the graph that connects two vertices. 
	graph.addEdge(Node(1), Node(2)); // key 1을 갖는 노드 -> key 2를 갖는 노드를 연결하는 Edge 추가
	
	// Adds a new, weighted, directed edge to the graph that connects two vertices.
	graph.addEdge(Node(3), Node(2), 3); // key 1을 갖는 노드 -> key 2를 갖는 노드를 연결하는 r가중치 3을 갖는 Edge 추가

	// finds the vertex in the graph named vertKey
	graph.getVertex(3);
	graph.getVertex(7);

	// returns the list of all vertices in the graph
	Node* getList = graph.getVertices();
	for (int i = 0; i < 4; i++) { // return 받은 list의 내용 출력
		cout << getList[i].getKey() << " ";
	}
	cout << endl;

	// returns True for a statement of the from vertex in graph, if the given vertex is in the graph, False otherwise.
	if (graph.hasVert(Node(2))) {
		cout << "해당 vertex가 존재합니다." << endl;
	}
	else {
		cout << "해당 vertex가 존재하지 않습니다." << endl;
	}
	if (graph.hasVert(Node(7))) {
		cout << "해당 vertex가 존재합니다." << endl;
	}
	else {
		cout << "해당 vertex가 존재하지 않습니다." << endl;
	}

	// returns True for a statement of the from edge in graph, if the given edge is in the graph, False otherwise.
	if (graph.hasEdge(Edge(Node(1), Node(2)))) {
		cout << "해당 Edge가 존재합니다." << endl;
	}
	else {
		cout << "Edge가 존재하지 않습니다." << endl;
	}
	if (graph.hasEdge(Edge(Node(5), Node(2)))) {
		cout << "해당 Edge가 존재합니다." << endl;
	}
	else {
		cout << "해당 Edge가 존재하지 않습니다." << endl;
	}
	return 0;
}