#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> dist[1001];

struct path {
	int d;
	int v;

	bool operator < (const path& p) const {
		return d > p.d;
	}
};

vector<path> graph[1001];

int main() {
	int N, M, K;
	cin >> N >> M >> K;

	K;

	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		graph[a].push_back({ c, b });
	}

	priority_queue<path> pq;

	pq.push({ 0, 1 });

	while (!pq.empty()) {
		path p = pq.top();
		pq.pop();

		if (dist[p.v].size() >= K) {
			continue;
		}

		dist[p.v].push_back(p.d);

		for (int i = 0; i < graph[p.v].size(); i++) {
			int nv = graph[p.v][i].v;

			if (dist[nv].size() < K) {
				pq.push({ graph[p.v][i].d + p.d, nv });
			}
		}
	}

	for (int i = 1; i < N + 1; i++) {
		if (dist[i].size() < K) {
			printf("-1\n");
		}
		else {
			printf("%d\n", dist[i][K-1]);
		}
	}
	return 0;
}