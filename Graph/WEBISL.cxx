/*
	date: 21 05 2015
	stat NA
*/
	// two dfs traversals for finding SCC

#include <bits/stdc++.h>
using namespace std;
#define pb push_back

const int N = 1e7 + 2;

vector<int>* adj;
vector<int>* adjt;

int n,m;

stack<int> s;

int v[N];

void dfs(int i) {
	if (v[i]) return;
	v[i] = 1;
	vector<int>::iterator it = adj[i].begin();
	while (it != adj[i].end()) {
		if (!v[*it]) dfs(*it);
		++it;
	}
	s.push(i);
}

int minimum; 

void dfs2(int i) {
	minimum = min(minimum, i);
	v[i] = 1;
	vector<int>::iterator it = adjt[i].begin();
	while (it != adjt[i].end()) {
		if (!v[*it]) dfs2(*it);
		++it;
	}
}

int compid[N];

void solve() {
	memset(v, 0, sizeof(v));
	for (int i = 0; i < n; ++i) dfs(i);

	memset(v, 0, sizeof(v));
	while (!s.empty()) {
		int i = s.top();
		minimum = INT_MAX;
		dfs2(i);
		while (!s.empty() && v[s.top()]) {
			compid[s.top()] = minimum;
			s.pop();
		}
	}
	for (int i = 0; i < n; ++i) cout << compid[i] << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	
    freopen("input.txt", "r+", stdin);
    freopen("output.txt", "w+", stdout);

	cin >> n >> m;
	adj = new vector<int>[n+1];
	adjt = new vector<int>[n+1];
	int a, b;
	for (int i = 0; i < m; ++i) {
		cin >> a >> b;
		adj[a].pb(b);
		adjt[b].pb(a);
	}
	solve();

	return 0;
}
