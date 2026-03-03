#include <queue>
#include <unordered_map>
#define INF (~0U >> 2)

int max(int a, int b) {
    return a > b ? a : b;
}

using namespace std;

int dist[5000];

int capital, N;

int maxDist[5000];

// (dist, city, maxDist)
struct path {
    int dist, city, maxDist;

    bool operator < (const path& other) const {
        if (dist != other.dist) return dist > other.dist;
        return maxDist > other.maxDist;
    }
};

struct edge {
    int id;
	int dist;
	int end;
    bool isRemoved;
};

priority_queue<path> pq;

vector<edge> graph[5000];

bool needUpdate;

int parentEdge[5000];

// idEdge[id] = (sCity, idx)
unordered_map<int, pair<int, int>> idEdge;

void dijkstra(int start) {
	pq.push({ dist[start], start, maxDist[start] });
	while (!pq.empty()) {
		path p = pq.top();
		pq.pop();

		if (dist[p.city] != p.dist || p.maxDist != maxDist[p.city]) {
			continue;
		}

		for (int i = 0; i < graph[p.city].size(); i++) {
			if (graph[p.city][i].isRemoved) {
				continue;
			}
			edge e = graph[p.city][i];

			int nd = p.dist + e.dist;
			int md = max(p.maxDist, e.dist);

			if (dist[e.end] > nd || (dist[e.end] == nd && maxDist[e.end] > md)) {
				dist[e.end] = nd;
				maxDist[e.end] = md;
                parentEdge[e.end] = e.id;
				pq.push({ dist[e.end], e.end, maxDist[e.end] });
			}
		}
	}
}

void init(int NN, int mCapital, int K, int mId[], int sCity[], int eCity[], int mDistance[]) {
	N = NN, capital = mCapital;

	for (int i = 0; i < N; i++) {
		graph[i].clear();
	}
	idEdge.clear();

	for (int i = 0; i < K; i++) {
		graph[sCity[i]].push_back({ mId[i], mDistance[i], eCity[i], false });
		idEdge[mId[i]] = {sCity[i], graph[sCity[i]].size() - 1};
	}

	needUpdate = true;

	return;
}

void add(int mId, int sCity, int eCity, int mDistance) {
	graph[sCity].push_back({ mId, mDistance, eCity, false });
	idEdge[mId] = {sCity, graph[sCity].size() - 1};

	if (needUpdate) {
		return;
	}

	int nd = mDistance + dist[sCity];
	int md = max(mDistance, maxDist[sCity]);

	if (dist[eCity] > nd || (dist[eCity] == nd && maxDist[eCity] > md)) {
		dist[eCity] = nd;
		maxDist[eCity] = md;
        parentEdge[eCity] = mId;
		dijkstra(eCity);
	}
	return;
}

void remove(int mId) {
	pair<int, int> p = idEdge[mId];
    
    graph[p.first][p.second].isRemoved = true;

    edge e = graph[p.first][p.second];

	if (parentEdge[e.end] == mId) {
        needUpdate = true;
    }
	return;
}

int calculate(int mCity) {
	if (needUpdate) {
		fill(dist, dist + N, INF);
		fill(maxDist, maxDist + N, 0);

		dist[capital] = 0;
		maxDist[capital] = 0;

		dijkstra(capital);

        needUpdate = false;
	}

	if (dist[mCity] == INF) {
		return -1;
	}
	else {
		return maxDist[mCity];
	}
}