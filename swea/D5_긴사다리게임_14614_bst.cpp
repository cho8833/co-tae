#include <set>
using namespace std;

#define LAST 1000000000

struct Node {
	int y;
	int x;
	Node* next;
	Node* prev;
};

struct Compare {
	bool operator()(const Node* a, const Node* b) const {
		return a->y > b->y;
	}
};

Node pool[400200];

int poolCnt;

set<Node*, Compare> rbTree[101];

Node* root[101];

Node* newNode(int y, int x) {
	Node* n = &pool[poolCnt++];
	n->y = y;
	n->x = x;
	n->next = nullptr;
	n->prev = nullptr;
	return n;
}

void init()
{
	poolCnt = 0;
	for (int i = 1; i < 101; i++) {
		Node* s = newNode(0, i);
		Node* e = newNode(LAST, i);
		s->next = e;
		e->prev = s;

		rbTree[i].clear();

		rbTree[i].insert(s);
		rbTree[i].insert(e);

		root[i] = s;
	}
}

void add(int mX, int mY)
{
	Node temp = { mY };
	
	Node* new_mx = newNode(mY, mX);
	Node* new_mx1 = newNode(mY, mX+1);

	Node* prev_mx = *rbTree[mX].lower_bound(&temp);
	Node* next_mx = prev_mx->next;

	Node* prev_mx1 = *rbTree[mX+1].lower_bound(&temp);
	Node* next_mx1 = prev_mx1->next;

	prev_mx->next = new_mx1;
	new_mx1->prev = prev_mx;

	prev_mx1->next = new_mx;
	new_mx->prev = prev_mx1;

	new_mx1->next = next_mx1;
	next_mx1->prev = new_mx1;

	new_mx->next = next_mx;
	next_mx->prev = new_mx;

	rbTree[mX].insert(new_mx);
	rbTree[mX + 1].insert(new_mx1);
}

void remove(int mX, int mY)
{
	Node temp = { mY };
	
	Node* target_mx = *rbTree[mX].find(&temp);
	Node* target_mx1 = *rbTree[mX + 1].find(&temp);

	Node* prev_mx = target_mx->prev;
	Node* prev_mx1 = target_mx1->prev;

	prev_mx->next = target_mx1->next;
	target_mx1->next->prev = prev_mx;

	prev_mx1->next = target_mx->next;
	target_mx->next->prev = prev_mx1;

	rbTree[mX].erase(&temp);
	rbTree[mX + 1].erase(&temp);
}

int numberOfCross(int mID)
{
	int answer = -1;

	Node* n = root[mID];
	while (n != nullptr) {
		answer++;
		n = n->next;
	}
	return answer - 1;
}

int participant(int mX, int mY)
{
	Node temp = { mY };
	Node* n = *rbTree[mX].lower_bound(&temp);

	while (n->prev != nullptr) {
		n = n->prev;
	}
	
	return n->x;
}