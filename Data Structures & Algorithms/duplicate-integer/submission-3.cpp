#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    std::unordered_set<int> Set;
    for(int num:nums) {
        if (Set.count(num)>0){
            return true;
        }
        Set.insert(num);
    }
    return false;  } 
};
