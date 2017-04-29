#include <iostream>
#include <string>

using namespace std;

struct node {
  int data[26][2]; // next index, count
};

const int N = 1e5;
node trie[N * 21];
int free_ptr = 1;

/**
 * Trie implementation using array
 * Recursive insert and lookup
 */
void add(string w, int wi = 0, int ptr = 0) {
  if (wi == w.length()) return ;
  int chr = w[wi] - 'a';
  if (trie[ptr].data[chr][1] == 0) {
    trie[ptr].data[chr][0] = free_ptr++;
  }
  trie[ptr].data[chr][1]++;
  add(w, wi + 1, trie[ptr].data[chr][0]);
}

int find(string w, int wi = 0, int ptr = 0) {
  int chr = w[wi] - 'a';
  if (wi == w.length() - 1) {
    return trie[ptr].data[chr][1];
  }
  if (trie[ptr].data[chr][1] == 0) return 0;
  return find(w, wi + 1, trie[ptr].data[chr][0]);
}

int main() {
  int n; cin >> n;
  while (n--) {
    string op; cin >> op;
    string w; cin >> w;
    if (op == "add") add(w);
    else cout << find(w) << endl;
  }

  return 0;
}
