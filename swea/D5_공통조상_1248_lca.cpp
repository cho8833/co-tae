#include <iostream>
#include <vector>

using namespace std;

vector<int> child[10001];

int parent[10001];

int level[10001];

int childCnt[10001];

void swap(int* a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int init(int n) {
    if (child[n].empty()) {
        return 1;
        childCnt[n] = 0;
    }

    int count = 0;
    for (int i = 0 ; i < child[n].size() ; i++) {
        int c = child[n][i];
        level[c] = level[n] + 1;

        count += init(c);
    }
    childCnt[n] = count + 1;
    return childCnt[n];
}

int main() {
    int T;
    cin >> T;
    parent[1] = -1;

    for (int t= 1 ; t < T+1 ; t++) {
        int V, E, a, b;
        cin >> V >> E >> a >> b;

        for (int i = 1 ; i < V+1 ; i++) {
            child[i].clear();
        }

        for (int i = 0 ; i < E ; i++) {
            int p, c;
            cin >> p >> c;

            child[p].push_back(c);
            parent[c] = p;
        }

        init(1);

        if (level[a] < level[b]) {
            swap(&a, &b);
        }

        while (level[b] != level[a]) {
            a = parent[a];
        }

        while (a != b) {
            a = parent[a];
            b = parent[b];
        }

        printf("#%d %d %d\n", t, a, childCnt[a]);
    }
}