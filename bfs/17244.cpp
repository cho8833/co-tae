#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int board[50][50];

int direction[][2] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}
};

bool visited[1 << 5][50][50] = {false ,};

int main() {
    int N, M;

    cin >> N >> M;

    int r, c, er, ec;

    int s_count = 0;

    for (int i = 0 ; i < M ; i++) {
        string input;
        cin >> input;
        for (int j = 0; j < N; j++) {
            switch (input[j])
            {
            case '#':
                board[i][j] = -2;
                break;
            case '.':
                board[i][j] = -1;
                break;
            case 'X':
                board[i][j] = s_count;
                s_count++;
                break;
            case 'S':
                r = i;
                c = j;
                board[i][j] = -1;
                break;
            case 'E':
                board[i][j] = -1;
                er = i;
                ec = j;
                break;
            }
        }
    }

    int answer = 15000;

    // for (int i = 0; i < M; i++) {
    //     for (int j = 0; j < N; j++) {
    //         cout << board[i][j] << " ";
    //     }
    //     cout << endl;
    // }
        // (r, c, d, state)
        queue<tuple<short, short, short, short>> q;
    q.push({r, c, 0, 0});

    while (!q.empty()) {

        tuple<short, short, short, short> p = q.front();
        q.pop();

        short r = get<0>(p);
        short c = get<1>(p);
        short d = get<2>(p);
        short state = get<3>(p);

        if (visited[state][r][c]) {
            continue;
        }

        if (d > answer) {
            continue;
        }

        visited[state][r][c] = true;

        if (board[r][c] > -1) {
            state = state | (1 << board[r][c]);
            visited[state][r][c] = true;
        }

        if (state == ((1 << s_count) - 1) && r == er && c == ec) {
            answer = d;
        }

        for (int i = 0 ; i < 4 ; i++) {
            short nr = direction[i][0] + r;
            short nc = direction[i][1] + c;

            if (nr > M-1 || nr < 0 || nc > N-1 || nc < 0 || visited[state][nr][nc] || board[nr][nc] < -1) {
                continue;
            }
            q.push({nr, nc, d+1, state});
        }

    }

    cout << answer;

    return 0;

}