#include <queue>
#include <unordered_map>
#define INF ~0U>>2
#define min(a,b) ((a) > (b)) ? (b) : (a)

using namespace std;

int dist[600][600];

struct Path {
	int next;
	int dist;
};

struct State {
	int dist;
	int node;
};

struct compare {
	bool operator () (const State& a, const State& b) const {
		return a.dist > b.dist;
	}
};

int cnt = 0;
unordered_map<int, int> comp;

int init(int N, int sCity[], int eCity[], int mCost[]) {

	cnt = 0;
	comp.clear();
	for (int i = 0; i < 600; i++) {
		for (int j = 0; j < 600; j++) {
			if (i == j) dist[i][j] = 0;
			else dist[i][j] = INF;
		}
	}

	for (int i = 0; i < N; ++i) {
		int s = sCity[i];
		int e = eCity[i];

		if (comp.find(s) == comp.end()) {
			comp[s] = cnt++;
		}
		if (comp.find(e) == comp.end()) {
			comp[e] = cnt++;
		}
		s = comp[s];
		e = comp[e];
		dist[s][e] = mCost[i];
	}

	
	for (int k = 0; k < cnt; k++) {
		for (int i = 0; i < cnt; i++) {
			for (int j = 0; j < cnt; j++) {
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
			}
		}
	}

	return cnt;
}

void add(int sCity, int eCity, int mCost) {
	sCity = comp[sCity];
	eCity = comp[eCity];
	for (int i = 0; i < cnt; i++) {
		for (int j = 0; j < cnt; j++) {
			dist[i][j] = min(dist[i][j], dist[i][sCity] + mCost + dist[eCity][j]);
		}
	}
	return;
}

int cost(int mHub) {
	int result = 0;
	mHub = comp[mHub];
	for (int i = 0; i < cnt; i++) {
		result += dist[mHub][i] + dist[i][mHub];
	}
	return result;
}