#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
using namespace std;

int **board;

int adj[][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };

int** newBoard(int N) {
    int length = 1 << N;

    int** board = new int*[length];
    for (int i = 0 ; i < length ; i++) {
        board[i] = new int[length];
    }
    return board;
}

void free(int** target, int N) {
    for (int i = 0 ; i < 1 << N ; i++) {
        delete[] target[i];
    }
    delete[] target;
}

int** copy(int N, int** target) {
    int len = 1 << N;

    int** nb = newBoard(N);

    for (int r = 0 ; r < 1 << N ; r++) {
        for (int c = 0 ; c < 1 << N ; c++) {
            nb[r][c] = target[r][c];
        }
    }
    return nb;
}

void div(int N, int L, int r, int c, int** nb) {
    if (L == N) {
        // rotate
        int len = 1 << L;
        int** target = newBoard(L);

        for (int i = r ; i < r + len ; i++) {
            for (int j = c ; j < c + len ; j++) {
                target[j-c][r+len-1-i] = board[i][j];
            }
        }
        
        // copy to new board with target
        for (int i = 0 ; i < len ; i++) {
            for (int j = 0 ; j < len ; j++) {
                nb[i+r][j+c] = target[i][j];
            }
        }
        free(target, L);
        return;
    }
    
    for (int i = r ; i < r + (1 << N) ; i += 1 << (N-1)) {
        for (int j = c ; j < c + (1 << N) ; j += 1 << (N-1)) {
            div(N-1, L, i, j, nb);
        }
    }
}

int** reduce(int N, int** nb) {
    int len = 1 << N;

    
    int** result = copy(N, nb);
    
    for (int r = 0 ; r < 1 << N ; r++) {
        for (int c = 0 ; c < 1 << N ; c++) {
            int count = 0;
            for (int a = 0 ; a < 4 ; a++) {
                int nr = adj[a][0] + r;
                int nc = adj[a][1] + c;

                if (nr > len - 1 || nr < 0 || nc > len - 1 | nc < 0) {
                    continue;
                }

                if (nb[nr][nc] > 0) {
                    count += 1;
                }
            }
            if (count < 3) {
                result[r][c] = max(result[r][c] - 1, 0);
            }
        }
    }
    return result;
}

int sum(int N) {
    int answer = 0;
    for (int i = 0 ; i < 1 << N ; i++) {
        for (int j = 0 ; j < 1 << N ; j++) {
            answer += board[i][j];
        }
    }
    return answer;
}

int dfs(int N) {
    int len = 1 << N;
    bool** visited = new bool*[len];

    for (int i = 0 ; i < len ; i++) {
        visited[i] = new bool[len] { false, };
    }

    int answer = 0;

    for (int r = 0 ; r < len ; r++) {
        for (int c = 0 ; c < len ; c++) {
            if (board[r][c] != 0 && !visited[r][c]) {
                // dfs
                vector<tuple<int, int>> q { make_tuple(r, c) };
                int temp = 0;
                while (!q.empty()) {
                    tuple<int, int> pos = q.back();

                    int r_ = get<0>(pos);
                    int c_ = get<1>(pos);

                    q.pop_back();

                    if (visited[r_][c_]) {
                        continue;
                    }
                    temp += 1;

                    visited[r_][c_] = true;


                    for (int i = 0 ; i < 4 ; i++) {
                        int nr = r_ + adj[i][0];
                        int nc = c_ + adj[i][1];

                        if (nr > len - 1 || nr < 0 || nc > len - 1 || nc < 0) {
                            continue;
                        }
                        if (board[nr][nc] > 0) {
                            q.push_back(make_tuple(nr,nc));
                        }

                    }   
                }
                answer = max(answer, temp);
            }
        }
    }

    free(visited);

    return answer;
}

int main() {
    int N, Q;
    cin >> N >> Q;
    
    board = newBoard(N);

    for (int i = 0 ; i < 1 << N ; i++) {
        for (int j = 0 ; j < 1 << N ; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 0 ; i < Q ; i++) {
        int L;
        cin >> L;
        
        // rotate
        int** nb = newBoard(N);
        div(N, L, 0, 0, nb);
        
        // reduce
        int** result = reduce(N, nb);

        free(nb);
        free(board);

        board = result;
        
    }

    cout << sum(N) << endl << dfs(N);
    return 0;

}