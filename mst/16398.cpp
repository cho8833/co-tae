#include <iostream>
#include <algorithm>
using namespace std;

struct path {
	int dist, a, b;

	bool operator < (path& p) {
		return dist < p.dist;
	}
};

path paths[500000];

int cnt = 0;

int parent[1000];

int find(int i) {
	if (parent[i] != i) {
		parent[i] = find(parent[i]);
	}
	return parent[i];
}

void merge(int a, int b) {
	a = find(a);
	b = find(b);

	if (a < b) {
		parent[b] = a;
	}
	else {
		parent[a] = b;
	}
}

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		parent[i] = i;
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int n;
			cin >> n;
			if (j <= i) {
				continue;
			}
			paths[cnt++] = { n, i, j };
		}
	}

	sort(paths, paths + cnt);

	long long answer = 0;

	for (int i = 0; i < cnt; i++) {
		path p = paths[i];
		if (find(p.a) != find(p.b)) {
			answer += p.dist;
			merge(p.a, p.b);
		}
	}
	cout << answer;
	return 0;
}