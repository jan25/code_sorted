#include <bits/stdc++.h>
using namespace std;

string a, b;
const int maxn = 10000;
int p[maxn];
set<int> vis;

int toInt(string& s) {
	int x = 0;
	for (int i = 0; i < 4; ++i) {
		x *= 10;
		x += s[i] - 48;
	}
	return x;
}

bool isPrime(string& s) {
	return p[toInt(s)] == 0;
}

bool visited(string& x) {
	return vis.find(toInt(x)) != vis.end();
}

void pushAll(queue<pair<string, int> >& q, string& s, int c) {
	for (int i = 0; i < 4; ++i) {
		int j = i == 0;
		int in = s[i];
		for (; j < 10; ++j) {
			s[i] = j + 48;
			if (!visited(s) && isPrime(s)) {
				vis.insert(toInt(s));
				q.push(make_pair(s, c + 1));
			}
		}
		s[i] = in;
	}
}

void solve() {
	vis.clear();
	queue<pair<string, int> > q;
	q.push(make_pair(a, 0));
	while (!q.empty()) {
		string s = q.front().first;
		int c = q.front().second;
		q.pop();	  	
		if (s == b) {
			cout << c;
			return ;
		}
		pushAll(q, s, c);
	}
	cout << "Impossible";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	for (int i = 2; i < maxn; ++i) {
		if (p[i]) continue;
		int j = i * i;
		while (j < maxn) {
			p[j] = 1;
			j += i;
		}
	}

	int t; cin >> t;
	while (t--) {
		cin >> a >> b;
		solve();
		cout << endl;
	}

	return 0;
}
