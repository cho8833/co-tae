#include <iostream>
#include <set>
#include <string>
using namespace std;

struct PAxis {
	int diff, x, y;
};

struct PCompare {
	bool operator () (const PAxis* a, const PAxis* b) const {
		if (a->diff == b->diff) return a->x < b->x;
		return a->diff < b->diff;
	}
};
struct MAxis {
	int sum, x, y;
};

struct MCompare {
	bool operator () (const MAxis* a, const MAxis* b) const {
		if (a->sum == b->sum) return a->x < b->x;
		return a->sum < b->sum;
	}
};

PAxis pPool[100000];
MAxis mPool[100000];

set<PAxis*, PCompare> pPlants;
set<MAxis*, MCompare> mPlants;

int main() {
	int N, K;
	cin >> N >> K;

	string jumps;
	cin >> jumps;

	int cnt = 0;

	PAxis first = { -1000000001, 0, 0 };
	PAxis last = { 1000000001, 0, 0 };
	pPlants.insert(&first);
	pPlants.insert(&last);

	MAxis mfirst = { -1000000001, 0, 0 };
	MAxis mlast = { 1000000001 , 0, 0 };
	mPlants.insert(&mfirst);
	mPlants.insert(&mlast);

	int xpos, ypos;
	cin >> xpos >> ypos;

	for (int i = 1; i < N; i++) {
		int x, y;
		cin >> x >> y;
		
		pPool[cnt] = { y - x, x, y };
		mPool[cnt] = { y + x, x, y };

		pPlants.insert(&pPool[cnt]);
		mPlants.insert(&mPool[cnt]);
		cnt++;
	}

	int j = 0;
	while (j < jumps.size()) {
		switch (jumps[j++]) {
		case 'A':
		{
			PAxis atemp = { ypos - xpos, xpos, ypos };
			PAxis* acheck = *pPlants.upper_bound(&atemp);
			if (acheck->diff != atemp.diff) {
				continue;
			}
			ypos = acheck->y;
			xpos = acheck->x;
			pPlants.erase(acheck);
			MAxis amTemp = { ypos + xpos, xpos };
			mPlants.erase(&amTemp);
			break;
		}
		case 'D':
		{
			PAxis dtemp = { ypos - xpos, xpos, ypos };
			PAxis* dcheck = *(--pPlants.lower_bound(&dtemp));
			if (dcheck->diff != dtemp.diff) {
				continue;
			}
			ypos = dcheck->y;
			xpos = dcheck->x;
			pPlants.erase(dcheck);
			MAxis bmTemp = { ypos + xpos, xpos };
			mPlants.erase(&bmTemp);
			break;
		}
		case 'B':
		{
			MAxis btemp = { ypos + xpos, xpos, ypos };
			MAxis* bcheck = *mPlants.upper_bound(&btemp);
			if (bcheck->sum != btemp.sum) {
				continue;
			}
			ypos = bcheck->y;
			xpos = bcheck->x;
			mPlants.erase(bcheck);
			PAxis cpTemp = { ypos - xpos, xpos };
			pPlants.erase(&cpTemp);
			break;
		}
		case 'C':
		{
			MAxis ctemp = { ypos + xpos, xpos, ypos };
			MAxis* ccheck = *(--mPlants.lower_bound(&ctemp));
			if (ccheck->sum != ctemp.sum) {
				continue;
			}
			ypos = ccheck->y;
			xpos = ccheck->x;
			mPlants.erase(ccheck);
			PAxis cpTemp = { ypos - xpos, xpos };
			pPlants.erase(&cpTemp);
			break;
		}
		}
	}

	printf("%d %d", xpos, ypos);
	return 0;
}