#include <iostream>
#include <queue>

#define MOD 20171109

using namespace std;


int main() {
	int T;
	cin >> T;
	for (int t = 1; t < T + 1; t++) {
		int N, A;
		cin >> N >> A;

		int answer = 0;

		priority_queue<int, vector<int>, greater<>> upper;
		priority_queue<int> lower;

		upper.push(A);

		for (int i = 0; i < N; i++) {
			int X, Y;
			cin >> X >> Y;

			if (upper.top() > X) {
				lower.push(X);
			}
			else {
				upper.push(X);
				lower.push(upper.top());
				upper.pop();
			}

			if (upper.top() < Y) {
				upper.push(Y);
			}
			else {
				lower.push(Y);
				upper.push(lower.top());
				lower.pop();
			}

			answer = (answer + upper.top()) % MOD;
		}

		printf("#%d %d\n", t, answer);
	}
}