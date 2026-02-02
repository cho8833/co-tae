#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

typedef tuple<int, int, int> fireball;

typedef vector<fireball> item;


// board[r][c] = { (질량, 속력, 방향), ...}

int direction[][2] = {
    {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}
};

item** newBoard(int N) {
    item** b = new item*[N];
    for (int i = 0 ; i < N ; i++) {
        b[i] = new item[N];
    }
    return b;

}

void free(int N, item** board) {
    for (int i = 0 ; i < N ; i++) {
        delete[] board[i];
    }
    delete[] board;
}

item** move(int N, item** board) {

    item** nb = newBoard(N);

    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            while (board[i][j].size() != 0) {
                fireball fire = board[i][j].back();
                board[i][j].pop_back();

                int m = get<0>(fire);
                int s = get<1>(fire);
                int d = get<2>(fire);

                int dr = direction[d][0] * s;
                int dc = direction[d][1] * s;

                int r = dr + i;
                int c = dc + j;

                if (r >= 0) {
                    r %= N;
                } else {
                    r = N-1 - (-r-1) % N;
                }
                if (c >= 0) {
                    c %= N;
                } else {
                    c = N -1 - (-c-1) % N;
                }
                nb[r][c].push_back(fire);
            }
        }
    }
    return nb;
}

item** mutate(int N, item** board) {
    item** nb = newBoard(N);
    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            if (board[i][j].size() > 1) {
                int weight_sum = 0;
                int speed_sum = 0;
                
                int firstDirection = get<2>(board[i][j][0]);
                bool isEven = firstDirection % 2 == 0;
                bool isSame = true;
    
                for (int f = 0 ; f < board[i][j].size() ; f++) {
                    // calc weight
                    weight_sum += get<0>(board[i][j][f]);
                    // calc speed
                    speed_sum += get<1>(board[i][j][f]);
                    // calc direction
                    if (isEven && get<2>(board[i][j][f]) % 2 != 0) {
                        isSame = false;
                    } else if (!isEven && get<2>(board[i][j][f]) % 2 != 1) {
                        isSame = false;
                    }
                }

                int weight = weight_sum / 5;

                if (weight == 0) {
                    continue;
                }

    
                
                int d = isSame ? 0 : 1;
                int speed = speed_sum / board[i][j].size();
                int until = d + 7;
                for ( ; d < until ; d+=2) {
                    nb[i][j].push_back(make_tuple(weight, speed, d));
                }
            } else {
                nb[i][j] = board[i][j];
            }
        }
    }

    return nb;
}

int main() {

    int N, M, K;
    cin >> N >> M >> K;

    item** board = newBoard(N);

    for (int i = 0 ; i < M ; i++) {
        int r, c, m, s, d;
        scanf("%d %d %d %d %d", &r, &c, &m, &s, &d);

        board[r-1][c-1].push_back(make_tuple(m,s,d));
    }

    for (int i = 0 ; i < K ; i++) {
        item** nb1 = move(N, board);
        free(board);

        item** nb2 = mutate(N, nb1);
        free(nb1);

        board = nb2;
    }

    int answer = 0;

    for (int r = 0 ; r < N ; r++) {
        for (int c = 0 ; c < N ; c++) {
            for (int f = 0 ; f < board[r][c].size() ; f++) {
                answer += get<0>(board[r][c][f]);

            }
        }
    }

    cout << answer;

    return 0;

}