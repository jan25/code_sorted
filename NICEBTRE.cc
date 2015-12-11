// http://www.spoj.com/problems/NICEBTRE/
/*
  O(n) to get height of tree, given inorder traversal
*/

#include <bits/stdc++.h>
using namespace std;
#define ii pair<int,int>

string s;

ii solve(int st = 0) {
	if (s[st] == 'l') return ii(1, 0); // size height
	ii pl = solve(st + 1);
	ii pr = solve(st + 1 + pl.first);
	return ii(pl.first + 1 + pr.first, max(pr.second, pl.second) + 1);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t; cin >> t;
	while (t--) {
		cin >> s;
		cout << solve().second << endl;
	}

	return 0;
}
