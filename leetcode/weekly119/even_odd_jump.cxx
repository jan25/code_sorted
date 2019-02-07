class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        map<int, int> map_to_smallest_index;
        
        map<int, int> next_even;
        map<int, int> next_odd;
        for (int i = A.size() - 1; i >= 0; --i) {
            next_even[i] = i; // self edge
            next_odd[i] = i; // self edge
            
            // for even
            auto it = map_to_smallest_index.upper_bound(A[i]);
            if (map_to_smallest_index.size() > 0 and it != map_to_smallest_index.begin()) {
                next_even[i] = (--it)->second;
            }
            
            // for odd
            it = map_to_smallest_index.lower_bound(A[i]);
            if (it != map_to_smallest_index.end()) {
                next_odd[i] = it->second;
            }
            
            map_to_smallest_index[A[i]] = i;
        }
        
        int possibles = 0;
        vector<pair<int, int> > memo(A.size(), pair<int, int>(-1, -1));
        for (int i = 0; i < A.size(); ++i)
            possibles += this->search(i, 1, next_odd, next_even, memo);
        return possibles;
    }
    
    int search(int v, int odd, map<int, int>& g_odd, map<int, int>& g_even, vector<pair<int, int> >& vis) {
        if (v == vis.size() - 1) return 1;
        
        if (odd and vis[v].first != -1) return vis[v].first;
        if (!odd and vis[v].second != -1) return vis[v].second;
        
        if (odd and g_odd[v] == v) return 0;
        if (!odd and g_even[v] == v) return 0;
        
        int next_v = odd ? g_odd[v] : g_even[v];
        int sol = this->search(next_v, odd ^ 1, g_odd, g_even, vis);
        
        if (odd) vis[v].first = sol;
        else vis[v].second = sol;
        return sol;
    }
};