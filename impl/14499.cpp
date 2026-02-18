#include <iostream>

using namespace std;

int board[20][20];

int direction[][2] = {
    {0, 0}, {0, 1}, {0, -1}, {-1, 0}, {1, 0}
};

int dice[4][3];

void roll(int d) {
    switch (d) {
        int temp;
        case 1:
            temp = dice[1][2];
            dice[1][2] = dice[1][1];
            dice[1][1] = dice[1][0];
            dice[1][0] = dice[3][1];
            dice[3][1] = temp;
            break;
        case 2:
            temp = dice[1][0];
            dice[1][0] = dice[1][1];
            dice[1][1] = dice[1][2];
            dice[1][2] = dice[3][1];
            dice[3][1] = temp;
            break;
        case 3:
            temp = dice[0][1];
            dice[0][1] = dice[1][1];
            dice[1][1] = dice[2][1];
            dice[2][1] = dice[3][1];
            dice[3][1] = temp;
            break;
        case 4:
            temp = dice[3][1];
            dice[3][1] = dice[2][1];
            dice[2][1] = dice[1][1];
            dice[1][1] = dice[0][1];
            dice[0][1] = temp;
            break;
    }
}

int main() {
    int N, M, x, y, K;

    cin >> N >> M >> y >> x >> K;

    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < M ; j++) {
            cin >> board[i][j];
        }
    }

    for (int k = 0 ; k < K ; k++) {
        int d;
        cin >> d;

        int ny = direction[d][0] + y;
        int nx = direction[d][1] + x;

        // 바깥쪽 이동 시도 시 무시
        if (nx > M-1 || nx < 0 || ny > N-1 || ny < 0) {
            continue;
        }
        x = nx;
        y = ny;

        roll(d);

        cout << dice[1][1] << endl;

        if (board[y][x] == 0) {
            board[y][x] = dice[3][1];
        } else {
            dice[3][1] = board[y][x];
            board[y][x] = 0;
        }
    }

    return 0;
}