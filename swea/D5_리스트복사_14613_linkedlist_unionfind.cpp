#include <unordered_map>
#include <string>

using namespace std;

short repos[10][200000];

struct Commit {
	int idx;
	short value;

	Commit* parent;
};

int repoCnt;
int commitCnt;
int branchCnt;

Commit commitPool[105010];

unordered_map<string, Commit*> branches;

unordered_map<string, string> parent;

unordered_map<string, int> branchRepo;

string find(string name) {
	if (name != parent[name]) {
		parent[name] = find(parent[name]);
	}
	return parent[name];
}

void merge(string dest, string src) {
	parent[dest] = find(src);
}

Commit* newCommit(int idx, int value, Commit* parent) {
	Commit* initial = &commitPool[commitCnt++];
	initial->idx = idx;
	initial->value = value;
	initial->parent = parent;

	return initial;
}

void init()
{
	repoCnt = 0;
	commitCnt = 0;
	branchCnt = 0;
}

// create branch and initial commit of repository
void makeList(char mName[], int mLength, int mListValue[])
{
	Commit* initial = newCommit(0, -1, nullptr);

	string name(mName);
	branches[name] = initial;
	parent[name] = name;
	branchRepo[name] = repoCnt;

	// copy values
	for (int i = 0; i < mLength; i++) {
		repos[repoCnt][i] = mListValue[i];
	}

	repoCnt++;
}

void copyList(char mDest[], char mSrc[], bool mCopy)
{
	string dest(mDest);
	string src(mSrc);
	src = find(src);

	// deep copy
	if (mCopy) {
		parent[dest] = dest;
		Commit* last = branches[src];
		Commit* node = newCommit(0, -1, last);

		branchRepo[dest] = branchRepo[src];

		branches[dest] = node;
	}
	// shallow copy
	else {
		merge(dest, src);
	}
}

// add new Commit
void updateElement(char mName[], int mIndex, int mValue)
{
	string name(mName);

	name = find(name);

	Commit* last = branches[name];

	Commit* commit = newCommit(mIndex, mValue, last);

	branches[name] = commit;
}

int element(char mName[], int mIndex)
{
	string name(mName);
	name = find(name);

	Commit* commit = branches[find(name)];
	int repo = branchRepo[name];
	

	while (commit->parent != nullptr) {
		if (commit->value == -1) {
			commit = commit->parent;
			continue;
		}
		if (mIndex == commit->idx) {
			return commit->value;
		}
		commit = commit->parent;
	}

	return repos[repo][mIndex];
}