#include <iostream>

using namespace std;

int board[100][100];

bool checkRow(int r, int N, int L) {
	int current = board[r][0];

	int cnt = 1;

	int c = 1;
	while (c < N) {
		if (board[r][c] == current) {
			cnt++;
			c++;
		}
		// 올라가는 경우
		else if (current+1 == board[r][c]) {
			if (cnt >= L) {
				current = board[r][c];
				cnt = 1;
				c++;
			}
			else {
				return false;
			}
		}
		// 내려가는 경우
		else if (current-1 == board[r][c]) {
			int fCnt = 1;
			int fCurrent = board[r][c];
			c++;
			while (c < N) {
				if (fCnt == L) {
					break;
				}
				if (board[r][c] == fCurrent) {
					fCnt++;
					c++;
				}
				else {
					break;
				}
			}
			if (fCnt == L) {
				if (c < N && fCurrent + 1 == board[r][c]) {
					return false;
				}
				cnt = 0;
				current = fCurrent;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}
	return true;
}

bool checkCol(int c, int N, int L) {
	int current = board[0][c];

	int cnt = 1;

	int r = 1;
	while (r < N) {
		if (board[r][c] == current) {
			cnt++;
			r++;
		}
		// 올라가는 경우
		else if (current + 1 == board[r][c]) {
			if (cnt >= L) {
				current = board[r][c];
				cnt = 1;
				r++;
			}
			else {
				return false;
			}
		}
		// 내려가는 경우
		else if (current - 1 == board[r][c]) {
			int fCnt = 1;
			int fCurrent = board[r][c];
			r++;
			while (r < N) {
				if (fCnt == L) {
					break;
				}
				if (board[r][c] == fCurrent) {
					fCnt++;
					r++;
				}
				else {
					break;
				}
			}
			if (fCnt == L) {
				if (r < N && fCurrent + 1 == board[r][c]) {
					return false;
				}
				cnt = 0;
				current = fCurrent;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}
	return true;
}


int main() {
	int N, L;
	cin >> N >> L;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}
	int answer = 0;

	for (int r = 0; r < N; r++) {
		if (checkRow(r, N, L)) {
			answer++;

		}
	}

	for (int c = 0; c < N; c++) {
		if (checkCol(c, N, L)) {
			answer++;

		}
	}

	cout << answer;
	return 0;

}