#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;

/**
* O(N) Algorithm
* Linear string scan
*/
class Solution {
public:
  int numJewelsInStones(string J, string S) {
    unordered_set<char> jewels;
    for (int i = 0; i < J.length(); ++i) {
      jewels.insert(J[i]);
    }

    int numJewels = 0;
    for (int i = 0; i < S.length(); ++i) {
      if (jewels.count(S[i]) > 0) numJewels++;
    }

    return numJewels;
  }
};

int main() {

  string j, s;
  cin >> j >> s;

  cout << ((new Solution())->numJewelsInStones(j, s)) << endl;

  return 0;
}