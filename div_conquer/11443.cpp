#include <iostream>

using namespace std;

typedef unsigned long long number;

number** base;

number** mm(number** mat1, number** mat2) {
    number** result = new number*[2];
    result[0] = new number[2];
    result[1] = new number[2];

    for (int i = 0 ; i < 2 ; i++) {
        for (int j = 0 ; j < 2 ; j++) {
            number temp = 0;
            for (int k = 0 ; k < 2 ; k++) {
                number t = mat1[i][k] * mat2[k][j];
                temp += ((mat1[i][k] * mat2[k][j]) % 1000000007);
            }
            result[i][j] = temp % 1000000007;
        }
    }

    return result;
}

number** div_pow(number n) {
    if (n == 1) {
        return base;
    }
    
    number** result = div_pow(n/2);

    if (n % 2 == 0) {
        return mm(result, result);
    } else {
        return mm(mm(result, result), base);
    }
}

int main() {

    // init
    base = new number*[2];
    base[0] = new number[2];
    base[1] = new number[2];
    base[0][0] = 1;
    base[0][1] = 1;
    base[1][0] = 1;
    base[1][1] = 0;

    number N;
    cin >> N;
    if (N % 2 == 1) {
        N--;
    }

    number** result = div_pow(N+1);

    cout << result[1][0] - 1;

    return 0;

}