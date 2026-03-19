#include <iostream>
#include <string>
#include <set>
using namespace std;

struct Album;
struct compare {
	bool operator() (const Album* a, const Album* b) const;
};

struct Album {
	string name;
	set<string> photos;
	set<Album*, compare> albums;
	Album* prev;
};


int cnt = 0;
Album pool[100000];

Album* newAlbum(string name, Album* prev) {
	Album* a = &pool[cnt++];
	a->name = name;
	a->prev = prev;
	return a;
}

inline bool compare::operator() (const Album* a, const Album* b) const {
	return a->name < b->name;
}

Album* current;
Album* root;

void mkalb(string S) {
	Album temp = { S };
	if (current->albums.find(&temp) == current->albums.end()) {
		current->albums.insert(newAlbum(S, current));
	}
	else {
		cout << "duplicated album name" << endl;
	}
}

pair<int, int> rmrf(Album* a) {
	int aResult = a->albums.size();
	int pResult = a->photos.size();
	for (set<Album*, compare>::iterator it = a->albums.begin(); it != a->albums.end(); it++) {
		pair<int, int> result = rmrf(*it);
		aResult += result.first;
		pResult += result.second;
	}
	return { aResult, pResult };
}

void rmalb(string S) {
	if (current->albums.size() == 0) {
		printf("0 0\n");
		return;
	}
	switch (S[0]) {
	case '-':
	{
		Album* t = *current->albums.begin();
		pair<int, int> result = rmrf(t);
		current->albums.erase(t);
		printf("%d %d\n", result.first+1, result.second);
		return;
	}
	case '0':
	{
		pair<int, int> result = { 0,0 };
		for (set<Album*, compare>::iterator it = current->albums.begin(); it != current->albums.end(); it++) {
			pair<int, int> r = rmrf(*it);
			result.first += r.first+1;
			result.second += r.second;
		}
		current->albums.clear();
		printf("%d %d\n", result.first, result.second);
		return;
	}
	case '1':
	{
		Album* t = *current->albums.rbegin();
		pair<int, int> result = rmrf(t);
		current->albums.erase(t);
		printf("%d %d\n", result.first+1, result.second);
		return;
	}
	default:
	{
		Album temp = { S };
		set<Album*, compare>::iterator it = current->albums.find(&temp);
		if (it == current->albums.end()) {
			printf("0 0\n");
			return;
		}
		pair<int, int> result = rmrf(*it);
		current->albums.erase(*it);
		printf("%d %d\n", result.first+1, result.second);
		return;
	}
	}
}

void insert(string S) {
	if (current->photos.find(S) == current->photos.end()) {
		current->photos.insert(S);
	}
	else {
		cout << "duplicated photo name" << endl;
	}
}

void del(string S) {
	if (current->photos.size() == 0) {
		printf("0\n");
		return;
	}
	switch (S[0]) {
	case '-':
	{
		current->photos.erase(*current->photos.begin());
		printf("1\n");
		return;
	}
	case '0':
	{
		printf("%d\n", current->photos.size());
		current->photos.clear();
		return;
	}
	case '1':
	{
		current->photos.erase(*current->photos.rbegin());
		printf("1\n");
		return;
	}
	default:
	{
		auto it = current->photos.find(S);
		if (it == current->photos.end()) {
			printf("0\n");
			return;
		}
		current->photos.erase(*it);
		printf("1\n");
		return;
	}
	}
}

void ca(string S) {
	switch (S[0]) {
	case '.':
	{
		if (current == root) {
			break;
		}
		current = current->prev;
		break;
	}
	case '/':
	{
		current = root;
		break;
	}
	default:
	{
		Album temp = { S };
		set<Album*, compare>::iterator it = current->albums.find(&temp);
		if (it == current->albums.end()) {
			break;
		}
		current = *it;
	}
	}
	printf("%s\n", current->name.c_str());
}

int main() {
	int N;
	cin >> N;

	current = newAlbum("album", nullptr);
	root = current;
	for (int i = 0; i < N; i++) {
		char cmd[10];

		cin >> cmd;

		string S;
		cin >> S;
		switch (cmd[0]) {
		case 'm':
		{
			
			mkalb(S);
			break;
		}
		case 'r':
		{
			
			rmalb(S);
			break;
		}
		case 'i':
		{
			insert(S);
			break;
		}
		case 'd':
		{
			del(S);
			break;
		}
		case 'c':
		{
			ca(S);
			break;
		}
		}
	}

	return 0;
}