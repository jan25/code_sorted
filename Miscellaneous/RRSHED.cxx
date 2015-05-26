/*
    date: 26 05 2015
*/
// round robin sheduling
// used map + fenwick
// O(nlogn)

#include <bits/stdc++.h>
using namespace std;
#define ll long long

const int N = 50001;

int BIT[N];

void remove(int i) {
	while (i < N) {
		BIT[i] += 1;
		i += i & -i;
	}
}

int getBelow(int i) {
	int sum = 0;
	while (i > 0) {
		sum += BIT[i];
		i -= i & -i;
	}
	return sum;
}


int queueSize;

ll timeOfFinish[N];

vector<pair<ll, int> > M; // time ->  position

map<ll, int> same; // time -> same

void solve(int n) {
	memset(BIT, 0, sizeof(BIT));

	vector<pair<ll, int> >::iterator it = M.begin();
	ll lastMin = 0;
	ll removed = 0;
	ll prevSpent = 0;
	ll sameCount = 0;
	ll minTime;
	while (it != M.end()) {
		sameCount = same[it->first];
		minTime = it->first;
		vector<int> v;
		while (sameCount--) {
			timeOfFinish[it->second] = prevSpent + 
						    ((n) * (minTime - lastMin - 1)) + 
							it->second - getBelow(it->second);
									
			v.push_back(it->second);
			++it;	
		}
		removed = v.size();
		for (int i = 0; i < removed; ++i) remove(v[i]);

		prevSpent += n * (minTime - lastMin);
		lastMin = minTime;
		n -= same[minTime];
	}
	for (int i = 1; i <= queueSize; ++i) printf("%lld\n", timeOfFinish[i]);
}

int main() {
	freopen("input.txt", "r+", stdin);
    freopen("output.txt", "w+", stdout);


	ll a; scanf("%d", &queueSize);
	for (int i = 1; i <= queueSize; ++i) {
		scanf("%lld", &a);
		M.push_back(make_pair(a, i));
		same[a] += 1;
	}
	sort(M.begin(), M.end());
	solve(queueSize);

	return 0;
}
