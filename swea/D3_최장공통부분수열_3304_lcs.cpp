#include <iostream>
#include <string>
#define max2(a, b) ((a) > (b) ? (a) : (b))

using namespace std;

// dp[i][j] : s1[i] 에서 s2[j] 까지 가장 긴 수열의 길이 dp[i][j]
int dp[1001][1001];

int main() {
	int T;
	cin >> T;
	for (int t = 1; t < T + 1; t++) {
		string s1;
		string s2;
		cin >> s1 >> s2;

		for (int i = 1; i < s1.size()+1; i++) {
			fill(dp[i] + 1, dp[i] + s2.size()+1, 0);
		}
		// init
		for (int i = 1; i < s1.size() + 1; i++) {
			for (int j = 1; j < s2.size() + 1; j++) {
				if (s1[i-1] == s2[j-1]) {
					dp[i][j] = dp[i - 1][j - 1] + 1;
				}
				else {
					dp[i][j] = max2(dp[i - 1][j], dp[i][j - 1]);
				}
			}
		}

		printf("#%d %d\n", t, dp[s1.size()][s2.size()]);
	}
}