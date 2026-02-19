#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

int board[300][300];

int direction[][2] = {
	{1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}
};

bool visited[300][300];

// (r, c)
typedef pair<int, int> node;

vector<node> v;

void open(int r, int c, int N) {
	visited[r][c] = true;
	if (board[r][c] == 0) {
		for (int d = 0; d < 8; d++) {
			int nr = r + direction[d][0];
			int nc = c + direction[d][1];

			if (nr > N - 1 || nr < 0 || nc > N - 1 || nc < 0 || visited[nr][nc]) {
				continue;
			}
			open(nr, nc, N);
		}
	}
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t < T + 1; t++) {
		int N;
		cin >> N;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				char c;
				cin >> c;

				switch (c) {
				case '.':
					board[i][j] = 0;
					break;
				case '*':
					board[i][j] = -1;
					break;
				}
			}
		}

		for (int i = 0; i < N; i++) {
			fill(visited[i], visited[i] + N, false);
		}
		v.clear();

		int spaceCount = 0;
		int zeroCount = 0;
		// init around count
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (board[r][c] == 0) {
					int cnt = 0;
					for (int d = 0; d < 8; d++) {
						int nr = direction[d][0] + r;
						int nc = direction[d][1] + c;

						if (nr > N - 1 || nr < 0 || nc > N - 1 || nc < 0) {
							continue;
						}

						if (board[nr][nc] == -1) {
							cnt++;
						}
					}
					board[r][c] = cnt;
					spaceCount++;
					if (cnt == 0) {
						v.push_back({ r, c });
						zeroCount++;
					}
				}
			}
		}

		int answer = 0;

		for (int i = 0; i < zeroCount; i++) {
			int r = v[i].first;
			int c = v[i].second;

			if (!visited[r][c]) {
				answer++;
				open(r, c, N);
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] > 0 && !visited[i][j]) {
					answer++;
				}
			}
		}

		printf("#%d %d\n", t, answer);

	}
}