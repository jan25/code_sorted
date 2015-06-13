/*
    13 july 2015
*/

#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define isc(c) (c >= 'a' && c <= 'z')

char s[(const int)1e5 + 1];

int main() {
	s[0] = '3';
	int t; scanf("%d", &t);
	while (t--) {
		int len = 1;
		char c = gc();
		while (!isc(c)) c = gc();
		for (; isc(c);) {
			if (c != s[len - 1]) { 
				s[len] = c;
				++len;	
			}
			c = gc();
		}
		string ans = "YES\n";
		for (int i = 1, j = len - 1; i < j; ++i, --j) {
			if (s[i] != s[j]) {
				ans = "NO\n";
				break;
			}
		}
		cout << ans;
	}

	return 0;
}
