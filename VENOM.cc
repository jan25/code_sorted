/**
* logN for each test case
* http://www.spoj.com/problems/VENOM/
*/

#include <bits/stdc++.h>
using namespace std;

int h, p, a;

bool lt(long long n) {
  return 2 * h + 2 * n * a <= 
          p * (n + 1) * (n + 2);
}

int solve() {
  int l = 0, r = 1e4;
  while (l < r) {
    int mid = (l + r) >> 1;
    if (lt(mid)) r = mid;
    else l = mid + 1;
  }
  return l;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t; 
  scanf("%d", &t);
  while (t--) {
    scanf("%d %d %d", &h, &p, &a);
    printf("%d\n", 2 * solve() + 1);
  } 

  return 0;
}
