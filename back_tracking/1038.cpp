#include <iostream>
#include <queue>

typedef unsigned long long num;

using namespace std;

int main() {
    int N;
    cin >> N;

    if (N == 0) {
        cout << 0;
        return 0;
    }

    queue<num> q;

    int cnt = 1;

    for (int i = 1 ; i < 10 ; i++) {
        q.push(i);

        if (cnt == N) {
            cout << i;
            return 0;
        }
        cnt++;
    }

    while (!q.empty()) {
        num n = q.front();
        q.pop();

        for (int i = 0 ; i < (n % 10) ; i++) {
            num next = n * 10 + i;
            if (cnt == N) {
                cout << n * 10 + i;
                return 0;
            } else {
                q.push(next);
                cnt++;
            }
        }
    }

    cout << -1;
    return 0;
}