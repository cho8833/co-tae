#include <iostream>

using namespace std;

short source[100001];

short tree[400001];

int process(int n) {
	if (n > 0) {
		return 1;
	}
	else if (n < 0) {
		return -1;
	}
	else {
		return 0;
	}
}

int init(int start, int end, int i) {
	if (start == end) return tree[i] = source[start];

	int mid = (start + end) / 2;

	return tree[i] = init(start, mid, i * 2) * init(mid + 1, end, i * 2 + 1);
}

int update(int start, int end, int i, int target, int v) {
	if (target < start || end < target) return tree[i];

	if (start == end) return tree[i] = v;

	int mid = (start + end) / 2;

	return tree[i] = update(start, mid, i * 2, target, v) * update(mid + 1, end, i * 2 + 1, target, v);
}

int query(int start, int end, int i, int left, int right) {
	if (end < left || right < start) return 1;

	if (left <= start && end <= right) return tree[i];

	int mid = (start + end) / 2;

	return query(start, mid, i * 2, left, right) * query(mid + 1, end, i * 2 + 1, left, right);
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, K;

	while (cin >> N >> K) {
		for (int i = 1; i < N + 1; i++) {
			int n;
			cin >> n;
			source[i] = process(n);
		}

		init(1, N, 1);

		for (int k = 0; k < K; k++) {
			char cmd;
			cin >> cmd;

			if (cmd == 'C') {
				int i, V;
				cin >> i >> V;

				update(1, N, 1, i, process(V));
			}
			else {
				int i, j;
				cin >> i >> j;

				int result = query(1, N, 1, i, j);

				if (result > 0) {
					printf("+");
				}
				else if (result < 0) {
					printf("-");
				}
				else {
					printf("0");
				}
			}
		}

		printf("\n");
	}
	return 0;
}