#include <iostream>
#include <algorithm>

using namespace std;

int arr[10000];
int main()
{
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + N);

    long long answer = 0;

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            int target = -(arr[i] + arr[j]);

            int start = lower_bound(arr + j + 1, arr + N, target) - arr;
            int end = upper_bound(arr + j + 1, arr + N, target) - arr;
            answer += (end - start);
        }
    }

    cout << answer;

    return 0;
}