#include <iostream>
#include <sstream>

using namespace std;

int ip[1000][4][8];

int mask[4][8];
int network[4][8];

int result_mask[4];
int result_network[4];

void calc(int N) {
	for (int p = 0; p < 4; p++) {
		for (int c = 0; c < 8; c++) {
			bool masked = true;
			int first = ip[0][p][c];
			for (int n = 1; n < N; n++) {
				if (first != ip[n][p][c]) {
					return;
				}
			}
			mask[p][c] = 1;
			network[p][c] = first;
		}
	}
}

int main() {
	int N;
	cin >> N;

	for (register int i = 0; i < N; i++) {
		string input;
		cin >> input;

		istringstream ss(input);

		int c = 0;
		string buffer;
		while (getline(ss, buffer, '.')) {
			int n = stoi(buffer);


			int p = 7;
			while (n != 0) {
				ip[i][c][p--] = n % 2;
				n = n / 2;
			}
			++c;
		}
	}

	calc(N);

	for (int p = 0; p < 4; p++) {
		int network_calc = 0;
		int mask_calc = 0;
		int temp = 1;
		for (int c = 7; c > -1; --c) {
			network_calc += network[p][c] * temp;
			mask_calc += mask[p][c] * temp;
			temp *= 2;
		}

		result_network[p] = network_calc;
		result_mask[p] = mask_calc;
	}

	for (int i = 0; i < 3; i++) {
		cout << result_network[i] << '.';
	}
	cout << result_network[3] << endl;

	for (int i = 0; i < 3; i++) {
		cout << result_mask[i] << '.';
	}
	cout << result_mask[3];

	return 0;
}