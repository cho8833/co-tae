#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> node;

vector<node> graph[10001];

priority_queue<node, vector<node>, greater<node>> pq;

int dist[10001];

bool visited[10001];

int INF = ~0U >> 2;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;

    for (int t = 0 ; t < T ; t++) {
        int N, D, C;
        cin >> N >> D >> C;

        fill(dist, dist + N + 1, INF);
        fill(visited, visited + N + 1, false);
        for (int i = 1 ; i < N+1 ; i++) {
            graph[i].clear();
        }

        for (int i = 0 ; i < D ; i++) {
            int a, b, s;
            cin >> a >> b >> s;

            graph[b].push_back({s, a});
        }

        int answer_time = 0;
        int answer_cnt = 0;

        dist[C] = 0;
        pq.push({0, C});

        while (!pq.empty()) {
            node t = pq.top();
            pq.pop();

            int d = t.first;
            int n = t.second;

            if (dist[n] != d) {
                continue;
            }

            answer_time = max(answer_time, d);

            if (!visited[n]) {
                visited[n] = true;
                answer_cnt++;
            }

            for (int i = 0 ; i < graph[n].size() ; i++) {
                int next = graph[n][i].second;
                int nd = graph[n][i].first;

                if (dist[next] > nd + d) {
                    dist[next] = nd + d;
                    pq.push({dist[next], next});
                }
            }
        }

        cout << answer_cnt << " " << answer_time << "\n";
    }
    return 0;
}