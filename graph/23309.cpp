#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int stations[1000001][2];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;

    cin >> N >> M;
    cin.ignore();

    string input;
    getline(cin, input);

    istringstream iss(input);

    vector<int> current;

    string token;
    while (iss >> token)
    {
        current.push_back(stoi(token));
    }

    stations[current.front()][0] = current.back();
    stations[current.front()][1] = current.at(1);

    for (int i = 1; i < current.size() - 1; i++)
    {
        stations[current[i]][0] = current.at(i - 1);
        stations[current[i]][1] = current.at(i + 1);
    }
    stations[current.back()][0] = current.at(current.size() - 2);
    stations[current.back()][1] = current.front();

    for (int i = 0; i < M; i++)
    {
        string cmd;
        cin >> cmd;

        if (cmd == "BN")
        {
            int i, j;
            cin >> i >> j;

            int next = stations[i][1];

            printf("%d\n", next);

            stations[i][1] = j;
            stations[next][0] = j;
            stations[j][0] = i;
            stations[j][1] = next;
        }
        else if (cmd == "BP")
        {
            int i, j;
            cin >> i >> j;

            int prev = stations[i][0];

            printf("%d\n", prev);

            stations[i][0] = j;
            stations[prev][1] = j;
            stations[j][0] = prev;
            stations[j][1] = i;
        }
        else if (cmd == "CN")
        {
            int i;
            cin >> i;

            int next = stations[i][1];

            printf("%d\n", next);

            stations[i][1] = stations[next][1];
            stations[stations[next][1]][0] = i;
        }
        else
        {
            int i;
            cin >> i;

            int prev = stations[i][0];

            printf("%d\n", prev);

            stations[i][0] = stations[prev][0];
            stations[stations[prev][0]][1] = i;
        }
    }

    return 0;
}