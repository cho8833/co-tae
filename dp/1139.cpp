#include <iostream>
#include <algorithm>

using namespace std;

pair<int, int> dp[10][1 << 13];

int jewels[13];

int main() {

    int N, M, C;

    cin >> N >> M >> C;

    for (int i = 0 ; i < N ; i++) {
        cin >> jewels[i];
    }

    // init
    for (int i = 0 ; i < N ; i++) {
        if (jewels[i] > C) {
            continue;
        }
        dp[0][1 << i] = make_pair(jewels[i], 1);
    }

    int answer = 0;

    // dp[m][jewel bit] = (weight, jewel count)
    for (int m = 0 ; m < M ; m++) {
        for (int j = 0 ; j < 1 << N ; j++) {
            if (dp[m][j].second > 0) {
                for (int b = 0 ; b < N ; b++) {
                    if (((1 << b) & j) == 0) { // b 보석이 포함되지 않은경우
                        // 넣을 수 있는 경우
                        if (C >= dp[m][j].first + jewels[b]) {
                            if (dp[m][j | (1 << b)].second < dp[m][j].second+1) {
                                dp[m][j | (1 << b)] = make_pair(dp[m][j].first + jewels[b], dp[m][j].second+1);
                            } else if (dp[m][j | (1 << b)].second == dp[m][j].second+1 && dp[m][j | (1<<b)].first > dp[m][j].first + jewels[b]) {
                                dp[m][j | (1 << b)] = make_pair(dp[m][j].first + jewels[b], dp[m][j | (1<<b)].second);
                            }
                        // 넣을 수 없는 경우
                        } else {
                            if (m < M-1) {
                                if (dp[m+1][j].second < dp[m][j].second) {
                                    dp[m+1][j] = make_pair(0, dp[m][j].second);
                                }
                            }
                        }
                    }
                }
                answer = max(answer, dp[m][j].second);
            }
        }
    }

    printf("%d", answer);
    return 0;

}