class Solution {
  List<int> twoSum(List<int> nums, int target) {
    var values = {};
    for (int i = 0; i < nums.length; i++){
        if (values[target - nums[i]] != null){
            return [values[target - nums[i]], i];
        }
        values[nums[i]] = i;
    } 
    return [0, 1];
  }
}