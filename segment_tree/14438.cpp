#include <iostream>
#define MAX 1000000001

using namespace std;

int source[100001];

int tree[400004];

int min(int a, int b) {
	if (a > b) return b;
	else return a;
}

int init(int start, int end, int i) {
	if (start == end) return tree[i] = source[start];

	int mid = (start + end) / 2;
	
	return tree[i] = min(init(start, mid, i * 2), init(mid + 1, end, i * 2 + 1));
}

int query(int start, int end, int i, int left, int right) {
	if (end < left || right < start) return MAX;

	if (left <= start && end <= right) return tree[i];

	int mid = (start + end) / 2;

	return min(query(start, mid, i * 2, left, right), query(mid + 1, end, i * 2 + 1, left, right));
}

int update(int start, int end, int i, int target, int v) {
	if (target < start || end < target) return tree[i];

	if (start == end) {
		return tree[i] = v;
	}
	
	int mid = (start + end) / 2;

	return tree[i] = min(update(start, mid, i * 2, target, v), update(mid + 1, end, i * 2 + 1, target, v));
}

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N;
	scanf("%d", &N);

	for (int i = 1; i < N + 1; i++) {
		scanf("%d", &source[i]);
	}

	init(1, N, 1);

	int M;
	scanf("%d", &M);

	for (int m = 0; m < M; m++) {
		int cmd, i, j;
		scanf("%d %d %d", &cmd, &i, &j);

		if (cmd == 2) {
			printf("%d\n", query(1, N, 1, i, j));
		}
		else {
			update(1, N, 1, i, j);
		}
	}
	return 0;
}