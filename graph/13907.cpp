#include <iostream>
#include <queue>
#include <vector>
#define INF ~0U >> 2
using namespace std;

struct Edge {
	int dist, next;
};

struct Path {
	int dist, node, count;
};

struct Compare {
	bool operator() (const Path& a,const Path& b) const {
		return a.dist > b.dist;
	}
};

int min(int a, int b) {
	return a > b ? b : a;
}

vector<Edge> graph[1000];

int dist[1001][1001];

void dijkstra(int S, int D) {
	priority_queue<Path, vector<Path>, Compare> pq;
	pq.push({ 0, S, 0 });
	dist[S][0] = 0;

	while (!pq.empty()) {
		Path p = pq.top();
		pq.pop();

		if (p.node == D) {
			continue;
		}
		if (dist[p.node][p.count] != p.dist) {
			continue;
		}

		for (int i = 0; i < graph[p.node].size(); i++) {
			int nd = graph[p.node][i].dist + p.dist;
			int next = graph[p.node][i].next;

			if (dist[next][p.count + 1] > nd) {
				dist[next][p.count + 1] = nd;
				pq.push({ nd, next, p.count + 1 });
			}
		}
	}
}

int main() {
	int N, M, K;
	cin >> N >> M >> K;

	int S, D;
	cin >> S >> D;

	for (int i = 1; i < N + 1; i++) {
		fill(dist[i], dist[i] + N, INF);
	}

	for (int i = 0; i < M; i++) {
		int a, b, w;
		cin >> a >> b >> w;

		graph[a].push_back({ w, b });
		graph[b].push_back({ w, a });
	}
	int total = 0;
	dijkstra(S, D);

	int answer = INF;

	for (int i = 0; i < N; i++) {
		if (dist[D][i] != INF) {
			answer = min(answer, dist[D][i]);
		}
	}

	cout << answer << endl;

	for (int i = 0; i < K; i++) {
		int p;
		cin >> p;

		total += p;

		answer = INF;

		for (int j = 0; j < N; j++) {
			if (dist[D][j] != INF) {
				answer = min(answer, dist[D][j] + total * j);
			}
		}

		cout << answer << endl;

	}

	return 0;

}