#include <queue>
#define max(a, b) ((a) > (b) ? (a) : (b))

using namespace std;

typedef pair<int, int> node;

int board[20][20];

int prediff[10000];

bool visited[20][20];

int direction[][2] = {
	{1, 0}, {-1, 0}, {0, -1}, {0, 1}
};

int N;

void init(int NN, int mMap[20][20])
{

	for (int i = 0; i < 10000; i++) {
		prediff[i] = 0;
	}
	N = NN;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			board[i][j] = mMap[i][j];
		}
	}

	for (int l = 2; l < 6; l++) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N - l+1; c++) {
				int current = board[r][c];
				int diff = 0;
				for (int k = 1; k < l; k++) {
					int next = board[r][c + k];
					int d = current - next + 5;

					diff = diff * 10 + d;

					current = next;
				}

				prediff[diff]++;
			}
		}

		for (int c = 0; c < N; c++) {
			for (int r = 0; r < N - l + 1; r++) {
				int current = board[r][c];
				int diff = 0;
				for (int k = 1; k < l; k++) {
					int next = board[r + k][c];
					int d = current - next + 5;

					diff = diff * 10 + d;

					current = next;
				}

				prediff[diff]++;
			}
		}
	}
}



int numberOfCandidate(int M, int mStructure[5])
{
	if (M == 1) {
		return N * N;
	}
	int diff = 0;
	int current = mStructure[0];
	for (int i = 1; i < M; i++) {
		int next = mStructure[i];
		int d = -(current - next) + 5;

		diff = diff * 10 + d;

		current = next;
	}

	int rDiff = 0;
	current = mStructure[M - 1];
	for (int i = M - 2; i > -1; i--) {
		int next = mStructure[i];
		int d = -(current - next) + 5;

		rDiff = rDiff * 10 + d;

		current = next;
	}

	if (diff == rDiff) {
		return prediff[diff];
	}
	else {
		return prediff[diff] + prediff[rDiff];
	}
}

int bfs(int seaLevel) {
	int answer = N * N;

	queue<node> q;

	for (int i = 0; i < N; i++) {
		fill(visited[i], visited[i] + N, false);
	}

	for (int c = 0; c < N - 1; c++) {
		if (board[0][c] < seaLevel) {
			q.push({ 0, c });
		}
	}

	for (int r = 0; r < N - 1; r++) {
		if (board[r][N - 1] < seaLevel) {
			q.push({ r, N - 1 });
		}
	}
	for (int c = N - 1; c > 0; c--) {
		if (board[N - 1][c] < seaLevel) {
			q.push({ N - 1, c });
		}
	}
	for (int r = N - 1; r > 0; r--) {
		if (board[r][0] < seaLevel) {
			q.push({ r, 0 });
		}
	}

	while (!q.empty()) {
		node n = q.front();
		q.pop();

		int r = n.first;
		int c = n.second;

		if (visited[r][c]) {
			continue;
		}

		visited[r][c] = true;
		answer--;

		for (int d = 0; d < 4; d++) {
			int nr = direction[d][0] + r;
			int nc = direction[d][1] + c;

			if (nr > N - 1 || nr < 0 || nc > N - 1 || nc < 0 || visited[nr][nc]) {
				continue;
			}
			if (board[nr][nc] < seaLevel) {
				q.push({ nr, nc });
			}
		}
	}
	return answer;
}

int maxArea(int M, int mStructure[5], int mSeaLevel)
{
	int answer = -1;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N - M + 1; c++) {
			// 0
			int check = board[r][c] + mStructure[0];
			bool isSame = true;
			for (int k = 1; k < M; k++) {
				if (board[r][c + k] + mStructure[k] != check) {
					isSame = false;
					break;
				}
			}

			if (isSame) {
				for (int k = 0; k < M; k++) {
					board[r][c + k] = check;
				}
				answer = max(answer, bfs(mSeaLevel));
				for (int k = 0; k < M; k++) {
					board[r][c + k] -= mStructure[k];
				}
			}

			// 180
			check = board[r][c] + mStructure[M - 1];
			isSame = true;
			for (int k = 1; k < M; k++) {
				if (board[r][c + k] + mStructure[M-k-1] != check) {
					isSame = false;
					break;
				}
			}

			if (isSame) {
				for (int k = 0; k < M; k++) {
					board[r][c + k] = check;
				}
				answer = max(answer, bfs(mSeaLevel));
				for (int k = 0; k < M; k++) {
					board[r][c + k] -= mStructure[M - k - 1];
				}
			}
		}
	}

	for (int c = 0; c < N; c++) {
		for (int r = 0; r < N - M + 1; r++) {
			// 90
			int check = board[r][c] + mStructure[0];
			bool isSame = true;
			for (int k = 1; k < M; k++) {
				if (board[r + k][c] + mStructure[k] != check) {
					isSame = false;
					break;
				}
			}

			if (isSame) {
				for (int k = 0; k < M; k++) {
					board[r + k][c] = check;
				}
				answer = max(answer, bfs(mSeaLevel));
				for (int k = 0; k < M; k++) {
					board[r + k][c] -= mStructure[k];
				}
			}

			// 270
			check = board[r][c] + mStructure[M - 1];
			isSame = true;
			for (int k = 1; k < M; k++) {
				if (board[r + k][c] + mStructure[M - 1 - k] != check) {
					isSame = false;
					break;
				}
			}
			if (isSame) {
				for (int k = 0; k < M; k++) {
					board[r + k][c] = check;
				}
				answer = max(answer, bfs(mSeaLevel));
				for (int k = 0; k < M; k++) {
					board[r + k][c] -= mStructure[M - k - 1];
				}
			}
		}
	}

	return answer;
}