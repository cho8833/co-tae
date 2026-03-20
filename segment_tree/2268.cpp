#include <iostream>

using namespace std;

int source[1000001];
long long tree[4000004];

long long sum(int start, int end, int left, int right, int i) {
	if (right < start || end < left) return 0;
	if (start >= left && right >= end) return tree[i];

	int mid = (start + end) / 2;
	return sum(start, mid, left, right, i * 2) + sum(mid + 1, end, left, right, i * 2 + 1);
}

void update(int start, int end, int i, int target, int diff) {
	if (target < start || target > end) return;
	tree[i] += diff;
	if (start == end) return;
	int mid = (start + end) / 2;
	update(start, mid, i * 2, target, diff);
	update(mid + 1, end, i * 2 + 1, target, diff);
	
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, M;
	scanf("%d %d", &N, &M);

	for (int m = 0; m < M; m++) {
		int cmd, i, j;
		scanf("%d %d %d", &cmd, &i, &j);

		if (cmd == 0) {
			if (i > j) {
				int temp = i;
				i = j;
				j = temp;
			}
			printf("%lld\n", sum(1, N, i, j, 1));
		}
		else {
			int diff = j - source[i];
			source[i] = j;
			update(1, N, 1, i, diff);
		}
	}

	return 0;
}