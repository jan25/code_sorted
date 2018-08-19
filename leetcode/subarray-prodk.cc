class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        
        long long numSubarrays = 0;
        int l = -1, r = 0;
        int currentProduct = nums[0];
        while (l <= r) {
            while (r < nums.size() - 1 && currentProduct * nums[r + 1] < k) {
                ++r;
                currentProduct *= nums[r];
            }
            numSubarrays += r - l;
        
            cout << numSubarrays<< endl;
            
            l++;
            if (l == nums.size()) break;
            currentProduct /= nums[l];
        }
        
        return numSubarrays;
    }
};