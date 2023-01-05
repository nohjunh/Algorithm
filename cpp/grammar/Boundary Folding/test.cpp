#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

int main() {
  string input;
	cin >> input;
	vector<string> str;
	stringstream ss(input);
	string temp;
	while (getline(ss, temp, '$')) {
		str.push_back(temp);
	}
	for (int i = 0; i < str.size() / 2; i++) {
		reverse(str[i].begin(), str[i].end());
		reverse(str[str.size() - 1 - i].begin(), str[str.size() - 1 - i].end());
	}
	int sum = 0;
	for (int i = 0; i < str.size(); i++) {
		sum += stoi(str[i]);
	}
	cout << sum << endl;

	return 0;
}
