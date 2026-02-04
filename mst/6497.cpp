#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int parent[200001];

tuple<int, int, int> h[200000];

int find(int a) {
    if (a != parent[a]) {
        parent[a] = find(parent[a]);
    }
    return parent[a];
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);

    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

int main() {

    int M, N;
    while (true) {
        scanf("%d %d", &M, &N);

        if (M == 0 && N == 0) {
            return 0;
        }

        int answer = 0;

        // init
        for (int i = 1 ; i < M+1 ; i++) {
            parent[i] = i;
        }

        // get path
        // (-z, x, y)
        for (int i = 0 ; i < N ; i++) {
            int x, y, z;
            scanf("%d %d %d", &x, &y, &z);

            h[i] = make_tuple(z, x, y);
        }

        sort(h, h+N);

        int size = 0;

        for (int i = 0 ; i < N ; i++) {
            tuple<int, int, int> t = h[i];
            int x = get<1>(t);
            int y = get<2>(t);

            if (find(x) != find(y)) {
                merge(x, y);
                size++;
            } else {
                answer += get<0>(t);
            }

            if (size == M-1) {
                for (int j = i+1 ; j < N ; j++) {
                    answer += get<0>(h[j]);
                }
                break;
            }
        }

        printf("%d\n", answer);

    }

    return 0;
}