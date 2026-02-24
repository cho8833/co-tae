#include <iostream>
#define max(a, b) ((a) > (b) ? (a) : (b))

using namespace std;

// dp[n][k] = n번째 물건을 넣을 때 넣을 수 있는 부피가 최대 k 일 때, 최대 가치 dp[n][k] 
int dp[101][1001];

// [부피, 가치]
int bags[101][2];

int main() {
	int T;
	cin >> T;
	for (int t = 1; t < T + 1; t++) {
		int N, K;
		cin >> N >> K;

		for (int i = 1; i < N+1; i++) {
			cin >> bags[i][0] >> bags[i][1];
		}
		
		for (int n = 1; n < N + 1; n++) {
			int v = bags[n][0];
			int c = bags[n][1];

			for (int k = 0; k < K + 1; k++) {
				if (k < v) {
					dp[n][k] = dp[n - 1][k];
				}
				else {
					dp[n][k] = max(dp[n-1][k], dp[n - 1][k - v] + c);
				}
			}

			
		}

		printf("#%d %d\n", t, dp[N][K]);
	}
}