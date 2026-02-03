#include <iostream>

using namespace std;

int board[499][499];

int** tornado[4];

int answer = 0;

int direction[][2] = {
    {0, -1}, {1, 0}, {0, 1}, {-1, 0}
};

void init_tornado() {
    int** t = new int*[5];
    t[0] = new int[5] {0,0,2,0,0};
    t[1] = new int[5] {0,10,7,1,0};
    t[2] = new int[5] {5,0,0,0,0};
    t[3] = new int[5] {0,10,7,1,0};
    t[4] = new int[5] {0,0,2,0,0};

    tornado[0] = t;

    for (int n = 1 ; n < 4 ; n++) {
        int** t = new int*[5];
        for (int i = 0 ; i < 5 ; i++) {
            t[i] = new int[5] {};
        }

        for (int i = 0 ; i < 5 ; i++) {
            for (int j = 0 ; j < 5 ; j++) {
                t[i][j] = tornado[n-1][j][4-i];
            }
        }

        tornado[n] = t;
    }
}

void move(int r, int c, int t, int N) {
    // t=0 -> 왼쪽, t=1 -> 아래쪽, t=2 -> 오른쪽, t=3 -> 위쪽
    int** tor = tornado[t];

    int sand = board[r][c];

    int moved = 0;

    for (int i = 0 ; i < 5 ; i++) {
        for (int j = 0 ; j < 5 ; j++) {
            int m = sand * tor[i][j] / 100;
            int nr = r + i - 2;
            int nc = c + j - 2;
            if (nr > N -1 || nr < 0 || nc > N-1 || nc < 0) {
                answer += m;
            } else {
                board[nr][nc] += m;
            }
            moved += m;
        }
    }

    board[r][c] = 0;
    int nr = r + direction[t][0];
    int nc = c + direction[t][1];
    int remain = sand - moved;

    if (nr > N-1  || nr < 0 || nc > N-1 || nc < 0) {
        answer += remain;
    } else {
        board[nr][nc] += remain;
    }
}


int main() {
    int N;
    cin >> N;

    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            cin >> board[i][j];
        }
    }

    init_tornado();

    int R = N / 2;

    int sr = N / 2;
    int sc = N / 2;

    for (int r = 0 ; r < R ; r++) {
        move(sr, --sc, 0, N);
        
        for (int i = 0 ; i < 2 + 2*r - 1 ; i++) {
            move(++sr, sc, 1, N);
        }
        
        for (int i = 0 ; i < 2 + 2*r ; i++) {
            move(sr, ++sc, 2, N);
        }
        for (int i = 0 ; i < 2 + 2*r ; i++) {
            move(--sr, sc, 3, N);
        }
        for (int i = 0 ; i < 2 + 2*r ; i++) {
            move(sr, --sc, 0, N);
        }
    }

    cout << answer;

    return 0;

}