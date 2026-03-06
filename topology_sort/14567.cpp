#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int indegree[1001];

int answer[1001];

vector<int> graph[1001];


struct path {
	int a;
	int i;
};
queue<path> q;

int main() {
	int N, M;
	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		int A, B;

		cin >> A >> B;

		indegree[B]++;
		graph[A].push_back(B);
	}

	for (int i = 1; i < N+1; i++) {
		if (indegree[i] == 0) {
			q.push({ 1, i });
		}
	}

	while (!q.empty()) {
		path p = q.front();
		q.pop();

		answer[p.i] = p.a;
		for (int i = 0; i < graph[p.i].size(); i++) {
			if (--indegree[graph[p.i][i]] == 0) {
				q.push({ p.a + 1, graph[p.i][i] });
			}
		}
	}

	for (int i = 1; i < N+1; i++) {
		cout << answer[i] << " ";
	}
	return 0;
	
}