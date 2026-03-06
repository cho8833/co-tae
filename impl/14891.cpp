#include <iostream>
#include <string>
using namespace std;

const int NI = 2, PI = 6;

int wheel[4][8];

void clockwise(int i) {
	int l = wheel[i][7];
	for (int j = 7; j > 0; j--) {
		int t = wheel[i][j];
		wheel[i][j] = wheel[i][j - 1];
		wheel[i][j - 1] = t;
	}
	wheel[i][0] = l;
}

void counterclockwise(int i) {
	int f = wheel[i][0];
	for (int j = 0; j < 7; j++) {
		int t = wheel[i][j];
		wheel[i][j] = wheel[i][j + 1];
		wheel[i][j + 1] = t;
	}
	wheel[i][7] = f;
}

int main() {
	for (int i = 0; i < 4; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < 8; j++) {
			wheel[i][j] = s[j] - '0';
		}
	}

	int K;
	cin >> K;

	for (int k = 0; k < K; k++) {
		int n, d;
		cin >> n >> d;
		n--;
		int rotate[4] = { 0, 0, 0, 0 };
		rotate[n] = d;

		// 왼쪽
		for (int i = n - 1; i > -1; i--) {
			if (wheel[i][NI] == wheel[i + 1][PI]) {
				break;
			}
			else {
				rotate[i] = rotate[i + 1] == -1 ? 1 : -1;
			}
		}
		// 오른쪽
		for (int i = n + 1; i < 4; i++) {
			if (wheel[i][PI] == wheel[i - 1][NI]) {
				break;
			}
			else {
				rotate[i] = rotate[i - 1] == -1 ? 1 : -1;
			}
		}

		// rotate
		for (int i = 0; i < 4; i++) {
			if (rotate[i] == -1) {
				counterclockwise(i);
			}
			else if (rotate[i] == 1) {
				clockwise(i);
			}
		}
	}
	
	int result = 0;
	for (int i = 0; i < 4; i++) {
		if (wheel[i][0] == 1) {
			result += 1 << i;
		}
	}
	cout << result;
	return 0;
}