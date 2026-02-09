#include <iostream>
#include <algorithm>

using namespace std;

int lis[100000];

int main() {
    int N;
    cin >> N;
    
    int length = 0;

    for (int i = 0 ; i < N ; i++) {
        int n;
        cin >> n;

        int idx = lower_bound(lis, lis+length, n) - lis;
        lis[idx] = n;
        if (idx == length) {
            length++;
        }
    }

    cout << N - length;

    return 0;
}