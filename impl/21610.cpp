#include <iostream>
#include <vector>

using namespace std;

int board[50][50];

int direction[][2] =  {
    {0,-1}, {-1,-1}, {-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}
};

int bugDirection[][2] = {
    {1, 1}, {-1, -1}, {1,-1}, {-1,1}
};

vector<vector<int>> move(vector<vector<int>> position, int d, int s, int N) {
    int dr = direction[d-1][0] * s;
    int dc = direction[d-1][1] * s;

    vector<vector<int>> newPosition;
    for (int i = 0 ; i < position.size() ; i++) {
        int r = position[i][0] + dr;
        int c = position[i][1] + dc;

        if (r >= 0) {
            r %= N;
        } else {
            r = N-1 - ((-r-1)%N);
        }
        if (c >= 0) {
            c %= N;
        } else {
            c = N-1 - ((-c-1)%N);
        }
        newPosition.push_back({r, c});
    }

    return newPosition;
}

void rain(vector<vector<int>> position) {
    for (int i = 0 ; i < position.size() ; i++) {
        board[position[i][0]][position[i][1]] += 1;
    }
}


void bug(vector<vector<int>> position, int N) {
    for (int i = 0 ; i < position.size() ; i++) {
        int r = position[i][0];
        int c = position[i][1];
        
        int count = 0;
        for (int d = 0 ; d < 4 ; d++) {
            int nr = r + bugDirection[d][0];
            int nc = c + bugDirection[d][1];

            if (nr > N-1 || nr < 0 || nc > N-1 || nc < 0) {
                continue;
            }
            if (board[nr][nc] > 0) {
                count += 1;
            }
        }

        board[r][c] += count;
    }
}

vector<vector<int>> reduce(vector<vector<int>> position, int N) {
    vector<int> temp;
    for (int i = 0 ; i < position.size() ; i++) {
        temp.push_back(board[position[i][0]][position[i][1]]);
        board[position[i][0]][position[i][1]] = 0;
    }

    vector<vector<int>> newPosition;

    for (int r = 0 ; r < N ; r++) {
        for (int c = 0 ; c < N ; c++) {
            if (board[r][c] > 1) {
                board[r][c] -= 2;
                newPosition.push_back({r, c});
            }
        }
    }

    for (int i = 0 ; i < position.size() ; i++) {
        board[position[i][0]][position[i][1]] = temp[i];
    }
    return newPosition;
}



int main() {
    int N, M;
    cin >> N >> M;

    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            cin >> board[i][j];
        }
    }

    vector<vector<int>> position = {
        {N-1, 0}, {N-1, 1}, {N-2, 0}, {N-2, 1}
    };
    

    for (int i = 0 ; i < M ; i++) {
        int d, s;
        cin >> d >> s;
        position = move(position, d, s, N);
        
        rain(position);

        bug(position, N);

        position = reduce(position, N);

    }

    int answer = 0;
    for (int r = 0 ; r < N ; r++) {
        for (int c = 0 ; c < N ; c++) {
            answer += board[r][c];
        }
    }

    cout << answer;

    return 0;
}