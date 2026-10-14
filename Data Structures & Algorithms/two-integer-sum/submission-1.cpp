class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>mappy;

        for (int i = 0; i < nums.size(); i++){
            mappy[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++){ 
            int diff = target - nums[i];

            if (mappy.count(diff)){
                if (i != mappy[diff]){
                    return {i, mappy[diff]};
                }
            }
        }

    }
};
