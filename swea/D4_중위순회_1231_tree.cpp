#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

struct Node {
	char c;
	Node* left;
	Node* right;
};

Node pool[101];

void inorder(Node* n) {
	if (n == nullptr) {
		return;
	}
	inorder(n->left);

	cout << n->c;

	inorder(n->right);
}

Node* newNode(int idx) {
	Node* node = &pool[idx];

	node->left = nullptr;
	node->right = nullptr;

	return node;
}

int main() {
	for (int t = 1; t < 11; t++) {
		int N;
		cin >> N;

		cin.ignore(1, '\n');
		for (int i = 0; i < N; i++) {
			char input[20];
			cin.getline(input, 20);

			char *token = strtok(input, " ");
			int n = 0;
			Node* node = nullptr;
			while (token) {
				switch (n) {
					case 0:
						node = newNode(stoi(token));
						break;
					case 1:
						node->c = token[0];
						break;
					case 2:
						node->left = &pool[stoi(token)];
						break;
					case 3:
						node->right = &pool[stoi(token)];
						break;
				}
				token = strtok(nullptr, " ");
				n++;
			}
		}

		printf("#%d ", t);

		inorder(&pool[1]);
		printf("\n");

	}

	return 0;
}