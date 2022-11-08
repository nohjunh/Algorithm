// Hashing
#include <iostream>
#include <string>
using namespace std;
const int M = 1234567891; // M의 값은 1234567891로 고정하자.
string str;
int L;

long long Hashing(string str) {
	long long hash = 0;
	long long r = 1; // 거듭제곱의 값인 r변수. r의 값은 31로 고정, 31^1 -> 31^2 ...
 
	for (int i = 0; i < L; i++) { // 문자열의 길이만큼 본다.
		hash = (hash + (str[i] - 'a' + 1) * r) % M; //str[i]-'a'을 해줌으로써 해당 알파벳의 int값을 대응
		r = (r * 31) % M; // 지수 증가 // 값이 너무 커지니까 유한한 출력을 가질 수 있도록 계속 mod M
	}

	return hash;
}

int main() {

	cin >> L; // 문자열의 길이 L이 들어온다.
	cin >> str; // 영문 소문자로만 이루어진 문자열이 들어온다.
	cout << Hashing(str)<<endl;
	return 0;
}