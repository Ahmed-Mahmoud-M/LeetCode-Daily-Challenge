#include<iostream>
#include<vector>

class Solution {
public:
    bool canSortArray(std::vector<int>& nums) {
        int n = nums.size();
        
        for(int i = 0; i < n - 1; i++) {
            for(int j = 0; j < n - i - 1; j++) {
                if ((countSetBits(nums[j]) == countSetBits(nums[j + 1])) && nums[j] > nums[j + 1]) {
                    std::swap(nums[j], nums[j + 1]);
                }   
            }
        }

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }

        return true;
    }

    unsigned int countSetBits(unsigned int num) {
        unsigned int count = 0;
        while (num) {
            count += num & 1;
            num >>= 1;
        }
        return count;
    }
};


int main(int argc, char const *argv[])
{
    Solution sol; 
    std::vector<int> nums = {8,4,2,30,15};

    std::cout << sol.canSortArray(nums) << std::endl;
    return 0;
}
