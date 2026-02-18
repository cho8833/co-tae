#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> cor;

int board[12][6];

int direction[][2] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}
};

bool visited[12][6];

int answer;

void push() {
    for (int c = 0 ; c < 6 ; c++) {
        queue<int> q;
        for (int r = 11 ; r > -1 ; r--) {
            if (board[r][c] > 0) {
                q.push(board[r][c]);
                board[r][c] = 0;
            }
        }

        int r = 11;
        while(!q.empty()) {
            int v = q.front();
            q.pop();
            board[r--][c] = v;
        }
    }
}

void calc() {
    for (int i = 0 ; i < 12 ; i++) {
        fill(visited[i], visited[i] + 6, false);
    }

    bool isDestroy = false;
    for (int r = 0 ; r < 12 ; r++) {
        for (int c = 0 ; c < 6 ; c++) {
            if (board[r][c] > 0 && !visited[r][c]) {
                // init bfs
                int current = board[r][c];
                int cnt = 0;
                queue<cor> q;
                q.push({r, c});

                queue<cor> cors;

                while (!q.empty()) {
                    cor n = q.front();
                    q.pop();

                    int rr = n.first;
                    int cc = n.second;

                    if (visited[rr][cc]) {
                        continue;
                    }

                    visited[rr][cc] = true;
                    cnt++;
                    cors.push({rr, cc});

                    for (int d = 0 ; d < 4 ; d++) {
                        int nr = rr + direction[d][0];
                        int nc = cc + direction[d][1];

                        if (nr > 11 || nr < 0 || nc > 5 || nc < 0 || visited[nr][nc] || board[nr][nc] != current) {
                            continue;
                        }
                        q.push({nr, nc});
                    }
                }

                // destroy
                if (cnt > 3) {
                    while(!cors.empty()) {
                        cor n = cors.front();
                        cors.pop();
                        board[n.first][n.second] = 0;
                    }
                    isDestroy = true;
                }
            }
        }
    }
    if (isDestroy) {
        push();
        answer++;
        calc();
    }
}

int main() {
    for (int i = 0 ; i < 12 ; i++) {
        string s;
        cin >> s;
        for (int j = 0 ; j < 6 ; j++) {
            char c = s[j];

            switch (c) {
                case '.':
                    board[i][j] = 0;
                    break;
                case 'R':
                    board[i][j] = 1;
                    break;
                case 'Y':
                    board[i][j] = 2;
                    break;
                case 'G':
                    board[i][j] = 3;
                    break;
                case 'P':
                    board[i][j] = 4;
                    break;
                case 'B':
                    board[i][j] = 5;
                    break;
            }
        }
    }

    calc();
    cout << answer;
    return 0;
}