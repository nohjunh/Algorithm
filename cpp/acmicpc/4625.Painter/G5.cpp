#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 12
using namespace std;

bool compare(int i, int j) {
	return j < i;
}

int main() {
	while (true) {
		int N, grayColor, kitNum;
		vector<int> PaintArray;
		cin >> N;
		if (N == 0) {
			exit(0);
		}
		for (int i = 0; i < N; i++) {
			int xml;
			cin >> xml;
			PaintArray.push_back(xml);
		}
		sort(PaintArray.begin(), PaintArray.end(), compare);

		int gogo = PaintArray.at(0) / 50;
		if (PaintArray.at(0) % 50 == 0) {
			kitNum = gogo;
		}
		else {
			kitNum = gogo + 1;
		}

		cin >> grayColor;
		vector<int> emptycolor;
		for (int i = 0; i < N; i++) {
			emptycolor.push_back((kitNum * 50) - PaintArray[i]);
		}
		while (true) {
			sort(emptycolor.begin(), emptycolor.end(), compare);
			if (grayColor <= 0) {
				break;
			}
			grayColor--;
			bool check = false;
			for (int i = 0; i < 3; i++) {
				emptycolor[i] = emptycolor[i] - 1;
			}
			for (int i = 0; i < 3; i++) {
				if (emptycolor[i] < 0) {
					check = true;
				}
			}
			if (check == true) {
				check = false;
				kitNum++;
				for (int i = 0; i < N; i++) {
					emptycolor[i] += 50;
				}
			}
		}
		cout << kitNum << endl;
	}

	return 0;
}