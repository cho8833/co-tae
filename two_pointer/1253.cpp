#include <iostream>
#include <algorithm>

using namespace std;

int arr[2000];

int main() {
    int N;
    cin >> N;
    
    for (int i = 0 ; i < N ; i++) {
        cin >> arr[i];
    }

    sort(arr, arr+N);

    int answer = 0;

    for (int i = 0 ; i < N ; i++) {
        int target = arr[i];

        int start = 0;
        int end = N-1;

        if (start == i) {
            start++;
        }
        if (end == i) {
            end--;
        }
        while (start < end) {
            int n = arr[start] + arr[end];

            if (n == target) {
                answer++;
                break;
            } else if (n > target) {
                end--;
                if (end == i) {
                    end--;
                }
            } else {
                start++;
                if (start == i) {
                    start++;
                }
            }
        }
    }

    cout << answer;
    return 0;
}