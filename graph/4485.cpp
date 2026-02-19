#include <iostream>
#include <queue>
using namespace std;

// (dist, r, c)
typedef pair<int, pair<short, short>> node;

int board[125][125];

int visited[125][125];

int INF = ~0U >> 2;

int direction[][2] = {
	{1, 0}, {-1, 0}, {0, -1}, {0, 1}
};

int main() {

	int T = 1;

	while (true) {
		int N;
		cin >> N;
		if (N == 0) {
			return 0;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> board[i][j];
			}
		}

		for (int i = 0; i < N; i++) {
			fill(visited[i], visited[i] + N, INF);
		}

		priority_queue<node, vector<node>, greater<node>> pq;

		visited[0][0] = board[0][0];
		pq.push({ board[0][0], {0, 0} });

		while (!pq.empty()) {
			node n = pq.top();
			pq.pop();

			int dist = n.first;
			int r = n.second.first;
			int c = n.second.second;

			if (dist != visited[r][c]) {
				continue;
			}

			if (r == N - 1 && c == N - 1) {
				printf("Problem %d: %d\n", T, dist);
				break;
			}

			for (int d = 0; d < 4; d++) {
				short nr = r + direction[d][0];
				short nc = c + direction[d][1];

				if (nr > N - 1 || nr < 0 || nc > N - 1 || nc < 0 || dist + board[nr][nc] >= visited[nr][nc]) {
					continue;
				}
				visited[nr][nc] = dist + board[nr][nc];
				pq.push({ dist + board[nr][nc],{ nr, nc} });
			}
		}
		T++;
	}
}