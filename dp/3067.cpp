#include <iostream>

using namespace std;

int main() {
    int T;

    cin >> T;

    for (int t = 0 ; t < T ; t++) {
        int N;

        cin >> N;

        int* coins = new int[N];

        for (int n = 0 ; n < N ; n++) {
            cin >> coins[n];
        }

        int M;

        cin >> M;

        int** dp = new int*[N];
        for (int i = 0 ; i < N ; i++) {
            dp[i] = new int[M+1] { 0, };
        }

        // init
        for (int i = 0 ; i < N ; i++) {
            dp[i][0] = 1;
        }
        int n = coins[0];
        while (n < M+1) {
            dp[0][n]++;
            n += coins[0];
        }


        for (int i = 1 ; i < N ; i++) {
            int coin = coins[i];
            for (int j = 1 ; j < M+1 ; j++) {
                if (j < coin) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    dp[i][j] = dp[i][j-coin] + dp[i-1][j];
                }
            }
        }

        cout << dp[N-1][M] << endl;
    } 

    return 0;
}