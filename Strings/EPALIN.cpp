/*
** 
**  Date:   18.04.2015
*/
// using K M P algorithm
//
#include <bits/stdc++.h>
#define gc getchar_unlocked
#define pc putchar_unlocked
#define isc(c) ( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') )
#define N 1e5+2
#define sf scanf

char s[2*N];
int tab[2*N];

void kmp() {
	int l = strlen(s);
	int i = 0, j = l+1;
	while (i != l) {
		s[j] = s[i];
		++i; ++j;
	}
	s[j] = '\0';
	--j;
	i = 1;
	while (i != l+1) {
		s[i] = s[j];
		--j; ++i;
	}
	tab[0] = -1;
	int k = -1;
	int L = l;
	l *= 2;
	int maxv = 0;
	for (int i = 1; i <= l; ++i) {
		while (k >= 0 && s[k+1] != s[i])
			k = tab[k];
		tab[i] = ++k;
	}
	
	i = L;
	++i;
	while (s[i] != '\0') pc(s[i++]);
	
	if (tab[l] == L) {
		pc('\n');
		return;
	}
	
	i = l-tab[l];
	while (i > L) {
		pc(s[i--]);
	}
	pc('\n');
	
}

int main() {
	while (sf("%s", s) == 1) {
		kmp();
	}
	return 0;
}
