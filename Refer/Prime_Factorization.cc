#include <bits/stdc++.h>
using namespace std;

/*
* Prime factorization trick using smallest prime factor for given n
* Modified sieve to store smallest prime factor for each n
* Factorization of number N in logN steps
*/

const int maxn = 1e6;
int p[maxn];
int sp[maxn];

int main() {

  for (int i = 2; i < maxn; ++i) {
    if (p[i]) continue;
    sp[i] = i;
    long long j = i;
    while (j * i < maxn) {
      if (!p[j * i]) {
        p[j * i] = 1;
        sp[j * i] = i;
      }
      ++j;
    }
  }

  int n; cin >> n;
  while (n > 1) {
    cout << sp[n] << " ";
    n /= sp[n];
    cout << n << endl;
  }

  return 0;
}
