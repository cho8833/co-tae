#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

short board[1000][1000];

int S[10];

queue<pair<int, int>> q[10];

int direction[][2] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}
};

int answer[10];

void tryFill(int n, int N, int M) {
    int size = q[n].size();

    queue<tuple<int, int, int>> nodes; 

    for (int i = 0 ; i < size ; i++) {
        pair<int, int> p = q[n].front();
        q[n].pop();
        
        for (int d = 0 ; d < 4 ; d++) {
            int nr = direction[d][0] + p.first;
            int nc = direction[d][1] + p.second;
            if (nr > N-1 || nr < 0 || nc > M-1 || nc < 0 || board[nr][nc] != 0) {
                continue;
            }
            nodes.push({1, nr, nc});
        }
    }

    while(!nodes.empty()) {
        tuple<int, int, int> node = nodes.front();
        nodes.pop();

        int r = get<1>(node);
        int c = get<2>(node);

        if (board[r][c] != 0) {
            continue;
        }
        board[r][c] = n;
        answer[n]++;

        int d = get<0>(node);
        if (d == S[n]) {
            q[n].push({r, c});
            continue;
        }

        for (int dd = 0 ; dd < 4 ; dd++) {
            int nr = direction[dd][0] + r;
            int nc = direction[dd][1] + c;
            if (nr > N-1 || nr < 0 || nc > M-1 || nc < 0 || board[nr][nc] != 0) {
                continue;
            }
            nodes.push({d+1, nr, nc});
        }
    }
    
    // for (int i = 0 ; i < N ; i++) {
    //     for (int j = 0 ; j < M ; j++) {
    //         cout << board[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    // cout << endl;
}

int main() {
    int N, M, P;
    cin >> N >> M >> P;

    for (int i = 1 ; i < P + 1 ; i++) {
        cin >> S[i];
    }

    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < M ; j++) {
            char c;
            cin >> c;
            switch (c) {
                case '.':
                    board[i][j] = 0;
                    break;
                case '#':
                    board[i][j] = -1;
                    break;
                default:
                    int n = c - '0';
                    board[i][j] = n;
                    q[n].push({i, j});
                    answer[n]++;
                    break;
            }
        }
    }

    while (true) {
        int cnt = 0;

        for (int i = 1 ; i < P +1 ; i++) {
            tryFill(i, N, M);
            cnt += q[i].size();
        }

        if (cnt == 0) {
            for (int n = 1 ; n < P + 1 ; n++) {
                cout << answer[n] << " ";
            }
            return 0;
        }
    }

    return 0;
}