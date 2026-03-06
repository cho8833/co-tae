#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

struct node {
	int r, c;
};

int board[50][50];

int visited[50][50];

int direction[][2] = {
	{1, 0}, {-1, 0}, {0, 1}, {0, -1}
};

int main() {
	int N, L, R;
	cin >> N >> L >> R;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	int answer = 0;

	while (true) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				visited[i][j] = false;
			}
		}

		bool moved = false;

		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (visited[r][c]) {
					continue;
				}
				queue<node> q;
				queue<node> result;

				q.push({ r, c });

				int total = 0;

				while (!q.empty()) {
					node n = q.front();
					q.pop();

					if (visited[n.r][n.c]) {
						continue;
					}
					visited[n.r][n.c] = true;
					total += board[n.r][n.c];
					result.push(n);

					for (int d = 0; d < 4; d++) {
						int nr = direction[d][0] + n.r;
						int nc = direction[d][1] + n.c;

						if (nr > N - 1 || nr < 0 || nc > N - 1 || nc < 0 || visited[nr][nc]) {
							continue;
						}
						int diff = abs(board[nr][nc] - board[n.r][n.c]);
						if (L <= diff && diff <= R) {
							q.push({ nr, nc });
						}
					}
				}
				if (result.size() > 1) {
					moved = true;
				}
				int v = total / result.size();
				while (!result.empty()) {
					node n = result.front();
					result.pop();
					board[n.r][n.c] = v;
				}
			}
		}
		if (!moved) {
			cout << answer;
			return 0;
		}
		answer++;
	}
}