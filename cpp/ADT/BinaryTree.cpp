#include <iostream>
#include <string>
using namespace std;

class BinaryNode{
private:
    int data; // val
    BinaryNode* left; // 왼쪽 자식 노드
    BinaryNode* right; // 오른쪽 자식 노드

public:
    // 초기화
    BinaryNode(int data=0, BinaryNode* left= nullptr, BinaryNode* right = nullptr){
        this->data = data; // data 기본 값은 0 
        this->left = left;
        this->right = right;
    }

    // setter, getter 설정
    void setData(int data) {  
        this->data = data; 
    }
    int getData() {
        return this->data; 
    }
    void setLeft(BinaryNode* left) {
        this->left = left;
    }
    BinaryNode* getLeft() { 
        return this->left; 
    }
    void setRight(BinaryNode* right) {
        this->right = right; 
    }
    BinaryNode* getRight() {
        return this->right; 
    }
    bool isLeaf() { // 리프노드인지 확인 (자식노드가 없는지 확인)
        return this->left == nullptr && this->right == nullptr;
    }
};

class BinaryTree{
private:
    BinaryNode* root;
    void removesNodes(BinaryNode* node);

    void preorder(BinaryNode* node);
    void inorder(BinaryNode* node);
    void postorder(BinaryNode* node);

    int getCountOfNodes(BinaryNode* node);
    int getHeight(BinaryNode* node);
public:
    BinaryTree() {
        this->root = nullptr; 
    }
    ~BinaryTree() { // 메모리 낭비 방지를 위해 설정된 node들 동적해제
        removesNodes(this->root);
    }
    bool isEmpty() { // BinaryTree가 비었는지 확인 -> root가 없으면 비어있다는 뜻
        return this->root == nullptr; 
    }
    // setter, getter
    void setRoot(BinaryNode* node) { // root를 설정해 binary Tree 뼈대 구축
        this->root = node; 
    }
    BinaryNode* getRoot() {  // 트리의 root 확인
        return this->root;
    }

    // traverse(order) 구현하기 위함.
    void traverse(string order);
    void preorder(); // 전위 순회
    void inorder(); // 중위 순회
    void postorder(); // 후위 순회
    int getCountOfNodes(); // return the number of nodes of tree

    // 트리의 높이는 서브 트리의 최대 높이 + 1
    int getHeight(); // returns the height of tree


    void addNode(BinaryNode* node, BinaryNode* isLeft) {
        if (isLeft->getLeft() == nullptr) { // isLeft의 왼쪽이 비어있다면, 즉 true 이면
            isLeft->setLeft(node);
        }
        else { // isLeft가 false 이면 오른쪽으로 넣어줘야 된다.
            isLeft->setRight(node);
        }
    }

    void addTree(BinaryTree* tree, BinaryNode* isLeft) {
        if (isLeft->getLeft() == nullptr) { // isLeft의 왼쪽이 비어있다면, 즉 true 이면
            isLeft->setLeft(tree->getRoot()); // 새로 추가할 트리의 루트를 isLeft의 왼쪽에 위치 시키면 됨.
        }
        else { // isLeft가 false 이면 오른쪽으로 넣어줘야 된다.
            isLeft->setRight(tree->getRoot()); // 새로 추가할 트리의 루트를 isLeft의 오른쪽에 위치 시키면 됨.
        }
    }
};

void BinaryTree::removesNodes(BinaryNode* node){ 
    // Linked로 연결하여 Tree를 구성하였기에
    // 왼쪽/오른쪽 서브 트리의 노드들이 동적해제가 먼저 된 후에 현재 노드를 해제해야 함.
    if (node != nullptr) {
        removesNodes(node->getLeft());
        removesNodes(node->getRight());
        delete node;
    }
}
// 객체지향 특성을 최대한 반영하기 위해 private, public function으로 나눠봄.
// 각 서브트리의 노드의 수와 자기 자신을 합하고 반환
int BinaryTree::getCountOfNodes() { // 트리 내에 있는 전체 노드의 수 세기
    return (this->isEmpty()) ? 0 : getCountOfNodes(this->root); // 삼항연산자로 구성.
    // empty면 노드가 없으므로 0, 그렇지 않으면 root부터 노드의 수 세기 시작.  
}
int BinaryTree::getCountOfNodes(BinaryNode *node) {
    if (node == nullptr) {
        return 0;
    }
    int cnt = getCountOfNodes(node->getLeft()); // 왼쪽 서브트리의 노드 갯수를 셈
    cnt += 1; // 자기 자신을 합함
    cnt += getCountOfNodes(node->getRight()); // 오른쪽 서브트리의 노드 갯수를 셈
    return cnt;
}

// 트리의 높이는 서브 트리의 최대 높이 + 1
int BinaryTree::getHeight(){
    return (this->isEmpty()) ? 0 : getHeight(root); // 위와 마찬가지로 root가 없으면 tree의 높이는 0
}
int BinaryTree::getHeight(BinaryNode *node) {
    if (node == nullptr || node->isLeaf()) {
        return 0;
    }
    int hLeft = getHeight(node->getLeft()); // 왼쪽 서브트리의 높이
    int hRight = getHeight(node->getRight()); // 오른쪽 서브트리의 높이
    return (hLeft > hRight) ? hLeft + 1 : hRight + 1; // 트리의 높이는 더 큰 서브트리 기준으로 세야 함.
}

// traverse(order) : 자료구조 내 데이터를 특정 순서대로 방문
void BinaryTree::traverse(string order) {
    if (order == "inorder") {  // 중위순회(in-order)
        inorder();
    }
    else if (order == "preorder") {  // 전위순회(pre-order)
        preorder();
    }
    else if (order == "postorder") {  // 후위순회(post-order)
        postorder();
    }
}

// 전위순회(pre-order)
void BinaryTree::preorder() {
    cout<< "preorder: ";
    preorder(this->root);
    cout<<endl;
}
void BinaryTree::preorder(BinaryNode* node) { // 루트출력 => 왼쪽 서브트리 => 오른쪽 서브트리
    if(node != nullptr){
        cout<< node->getData() << " "; // 루트출력
        preorder(node->getLeft()); // 왼쪽 서브트리 
        preorder(node->getRight()); // 오른쪽 서브트리
    }
}

// 중위순회(in-order)
void BinaryTree::inorder() { 
    cout<< "inorder: ";
    inorder(this->root);
    cout<<endl;
}
void BinaryTree::inorder(BinaryNode* node) {  // 왼쪽 서브트리 => 루트 출력 => 오른쪽 서브트리 
    if(node != nullptr){
        inorder(node->getLeft());  // 왼쪽 서브트리
        cout<< node->getData() << " "; // 루트 출력 
        inorder(node->getRight()); // 오른쪽 서브트리
    }
}

// 후위순회(post-order)
void BinaryTree::postorder() {
    cout<< "postorder: ";
    postorder(this->root);
    cout<<endl;
}
void BinaryTree::postorder(BinaryNode* node) { // 왼쪽 서브트리 => 오른쪽 서브트리 => 루트출력
    if(node != nullptr){
        postorder(node->getLeft());  // 왼쪽 서브트리
        postorder(node->getRight());  // 오른쪽 서브트리 
        cout<< node->getData() << " ";  // 루트 출력
    }
}


int main() {
    BinaryTree tree; // BinaryTree 생성
    // BinaryTree 상태 초기화
    /*
                     1
                2         3
             4     5   6  
    */
    BinaryNode* d = new BinaryNode(4, nullptr, nullptr);
    BinaryNode* e = new BinaryNode(5, nullptr, nullptr);
    BinaryNode* b = new BinaryNode(2, d, e); // 왼쪽 자식노드 d, 오른쪽 자식노드 e
    BinaryNode* f = new BinaryNode(6, nullptr, nullptr);
    BinaryNode* c = new BinaryNode(3, f, nullptr); // 왼쪽 자식노드 f
    BinaryNode* a = new BinaryNode(1, b, c); // 왼쪽 자식노드 b, 오른쪽 자식노드 c
    tree.setRoot(a); // a를 root로 하는 BinaryTree를 만든다.

    
    // add node on the left child node if isLeft is true, otherwise, add tree on the right child node if isLeft is false
    /*
                     1
                2         3
             4     5   6
         7      8
    */
    BinaryNode* g = new BinaryNode(7, nullptr, nullptr);
    BinaryNode* h = new BinaryNode(8, nullptr, nullptr);
    tree.addNode(g, d); // 노드 4의 왼쪽 자식노드에 연결될 것이다.
    tree.addNode(h, d); // 노드 4의 오른쪽 자식 노드에 연결될 것이다.

    
    // add tree on the left child node if isLeft is true, otherwise, add tree on the right child node if isLeft is false
    /*
                         1
                    2          3
                 4     5    6     9
             7      8          10   11
    */
    BinaryTree tree2; // 새로 추가할 트리 생성
    BinaryNode* k = new BinaryNode(11, nullptr, nullptr);
    BinaryNode* j = new BinaryNode(10, nullptr, nullptr);
    BinaryNode* i = new BinaryNode(9, j, k); // 왼쪽 자식노드 h, 오른쪽 자식노드 i
    tree2.setRoot(i);
    tree.addTree(&tree2, c); // 기존 트리 노드 3의 왼쪽 자식이 있으므로 오른쪽 자식으로 tree가 연결될 것이다.

    
    cout << "getCountOfNodes: " << tree.getCountOfNodes() << endl; // return the number of nodes of tree
    cout << "getHeight: " << tree.getHeight() << endl; // returns the height of tree
    //return the form of an expression for order
    tree.traverse("preorder");  // preorder
    tree.traverse("inorder");   // inorder
    tree.traverse("postorder");  // postorder
    return 0;
}