#define MOD 20
using namespace std;

int table[100010];
int preCalc[100010];
int jokerCnt[100010];

int joker;

int head, tail;

void calc(int i) {
	int result = 0;
	int cnt = 0;
	for (int j = 0; j < 4; j++) {
		if (table[i - j] == -1) {
			cnt++;
		}
		else {
			result += table[i - j];
		}
	}
	preCalc[i] = result % MOD;
	jokerCnt[i] = cnt;
}

void init(int mJoker, int mNumbers[5])
{
	joker = mJoker; 
	head = 49999;
	tail = 50000;

	for (int i = 0; i < 5; i++) {
		table[tail++] = mNumbers[i];
	}

	calc(50003);
	calc(50004);
}

void putCards(int mDir, int mNumbers[5])
{
	if (mDir == 1) {
		int li = tail;
		for (int i = 0; i < 5; i++) {
			table[tail++] = mNumbers[i];
			calc(li + i);
		}
	}
	else {
		for (int i = 4; i > -1; i--) {
			table[head--] = mNumbers[i];
			calc(head+4);
		}
	}
}

int findNumber(int mNum, int mNth, int ret[4])
{
	int th = 0;
	for (int i = head + 4; i < tail; i++) {
		if ((preCalc[i] + jokerCnt[i] * joker) % MOD == mNum) {
			if (++th == mNth) {
				for (int j = 0; j < 4; j++) {
					ret[j] = table[i - 3 + j];
				}
				return 1;
			}
		}
	}
	return 0;
}

void changeJoker(int mValue)
{
	joker = mValue;
}