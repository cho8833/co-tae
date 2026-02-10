#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int board[100][100];

bool visited[100][100];

int direction[][2] = {
    {1, 0}, {0, 1}, {0, -1}, {-1, 0}
};

void print(int R, int C) {
    for (int r = 0 ; r < R ; r++) {
        for (int c = 0 ; c < C ; c++) {
            cout << board[r][c];
        }
        cout << endl;
    }
    cout << endl;
}



pair<int, int> shoot(int C, int h, bool isLeft) {
    if (isLeft) {
        for (int c = 0 ; c < C ; c++) {
            if (board[h][c] > 0) {
                return {h, c};
            }
        }
    } else {
        for (int c = C-1 ; c > -1 ; c--) {
            if (board[h][c] > 0) {
                return {h, c};
            }
        }
    }
    return {-1, -1};
}

void push(int R, int C, int fr, int fc) {
    vector<pair<int, int>> v;
    vector<pair<int, int>> cluster[4];

    for (int i = 0 ; i < R ; i++) {
        fill(visited[i], visited[i] + C, false);
    }
    for (int d = 0 ; d < 4 ; d++) {
        int r = direction[d][0] + fr;
        int c = direction[d][1] + fc;

        if (r > R-1 || r < 0 || c > C-1 || c < 0 || board[r][c] == 0 || visited[r][c]) {
            continue;
        }

        v.push_back({r, c});

        bool bottom = false;
        while (!v.empty()) {
            pair<int, int> p = v.back();
            v.pop_back();
            int rr = p.first;
            int cc = p.second;

            if (visited[rr][cc]) {
                continue;
            }

            if (rr == R-1) {
                bottom = true;
            }

            visited[rr][cc] = true;
            cluster[d].push_back({rr, cc});

            for (int dd = 0 ; dd < 4 ; dd++) {
                int nr = rr + direction[dd][0];
                int nc = cc + direction[dd][1];

                if (nr > R-1 || nr < 0 || nc > C-1 || nc < 0 || visited[nr][nc] || board[nr][nc] == 0) {
                    continue;
                }
                v.push_back({nr, nc});
            }
        }
        if (bottom) {
            cluster[d].clear();
        }
    }
    for (int c = 0 ; c < 4 ; c++) {
        if (!cluster[c].empty()) {
            for (int i = 0 ; i < cluster[c].size() ; i++) {
                board[cluster[c][i].first][cluster[c][i].second] = 0;
            }
            int l = 1;
            while (true) {
                bool push = true;
                for (int i = 0 ; i < cluster[c].size() ; i++) {
                    int dr = cluster[c][i].first + l;
                    if (dr > R-1 || board[dr][cluster[c][i].second] > 0) {
                        push = false;
                        break;
                    }
                }
                if (push) {
                    l++;
                } else {
                    l--;
                    while (!cluster[c].empty()) {
                        pair<int, int> p = cluster[c].back();
                        cluster[c].pop_back();
                        board[p.first + l][p.second] = 1;
                    }
                    break;
                }
            }
        }
    }

    // print(R, C);
}

int main() {
    int R, C;
    cin >> R >> C;

    for (int r = 0 ; r < R ; r++) {
        for (int c = 0 ; c < C ; c++) {
            char i;
            cin >> i;
            switch (i) {
                case '.':
                    board[r][c] = 0;
                    break;
                case 'x':
                    board[r][c] = 1;
                    break;
            }
        }
    }

    int N;
    cin >> N;
    bool isLeft = true;
    for (int n = 0 ; n < N ; n++) {
        int h;
        cin >> h;

        pair<int, int> found = shoot(C, R - h, isLeft);
        isLeft = !isLeft;
        int fr = found.first;
        int fc = found.second;
        if (fr == -1 && fc == -1) {
            continue;
        }

        // destroy
        board[fr][fc] = 0;

        push(R, C, fr, fc);
    }

    for (int r = 0 ; r < R ; r++) {
        for (int c = 0 ; c < C ; c++) {
            if (board[r][c] > 0) {
                cout << 'x';
            } else {
                cout << '.';
            }
        }
        cout << endl;
    }
    return 0;

}