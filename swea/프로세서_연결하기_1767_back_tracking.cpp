#include <iostream>
#include <algorithm>

using namespace std;

int direction[][2] = {
	{1, 0}, {0, 1}, {-1, 0}, {0, -1}
};

int board[12][12];

int maxConnect;

int answer;

typedef pair<int, int> node;

node cores[12];

void bt(int N, int total, int len, int i, int count, int connect) {
	if (count == total) {
		if (maxConnect < connect) {
			answer = len;
			maxConnect = connect;
		}
		else if (maxConnect == connect) {
			answer = min(answer, len);
		}
		return;
	}

	// prunning
	if (connect + total-count < maxConnect) {
		return;
	}

	for (int core = i; core < total; core++) {

		int r = cores[core].first;
		int c = cores[core].second;

		for (int d = 0; d < 4; d++) {
			bool isConnected = true;

			int nr = r;
			int nc = c;

			int length = 0;

			nr += direction[d][0];
			nc += direction[d][1];
			while (nr < N && nr > -1 && nc < N && nc > -1) {

				if (board[nr][nc] != 0) {
					isConnected = false;
					break;
				}
				else {
					board[nr][nc] = -1;
					length++;
				}
				nr += direction[d][0];
				nc += direction[d][1];
			}

			if (isConnected) {
				bt(N, total, length + len, core + 1, count+1, connect+1);
			}

			// back track
			nr -= direction[d][0];
			nc -= direction[d][1];
			while (nr != r || nc != c) {
				board[nr][nc] = 0;
				nr -= direction[d][0];
				nc -= direction[d][1];
			}
		}
		bt(N, total, len, core + 1, count + 1, connect);

	}
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t < T + 1; t++) {
		int N;
		cin >> N;

		int num = 0;

		answer = ~0U >> 2;
		maxConnect = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int n;
				cin >> n;
				if (n == 0) {
					board[i][j] = 0;
				}
				else {
					board[i][j] = 1;
					if (i == 0 || i == N - 1 || j == 0 || j == N - 1) {
						continue;
					}
					cores[num++] = { i, j };
				}
			}
		}

		bt(N, num, 0, 0, 0, 0);

		printf("#%d %d\n", t, answer);
	}
}