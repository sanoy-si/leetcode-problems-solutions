/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var partitionArray = function(nums, k) {
  nums.sort((a, b) => a - b);
  let left = 0, count = 1;
   
  for (let right = 0; right < nums.length; right++){
    if (nums[right] - nums[left] > k){
        count += 1;
        left = right;
    }
  }
   
   return count;
};