#include <iostream>
#include <algorithm>

using namespace std;

int dp[101][100001] = { 0, };

int stime[101];

int score[101];

int main() {

    int N, T;
    cin >> N >> T;

    for (int i = 1 ; i < N+1 ; i++) {
        int K, S;

        cin >> K >> S;

        stime[i] = K;

        score[i] = S;
    }


    for (int i = 1 ; i < N + 1 ; i++) {
        int s = score[i];
        int t = stime[i];
        for (int j = 1 ; j < T+1 ; j++) {
            if (t > j) {
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-t] + s);
            }
        }
    }
    cout << dp[N][T];
    return 0;
}