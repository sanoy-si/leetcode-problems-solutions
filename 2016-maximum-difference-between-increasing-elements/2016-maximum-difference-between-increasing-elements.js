/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let answer = -1, current_minimum = nums[0];
    for (let i = 1; i < nums.length; i++){
        answer = Math.max(answer, nums[i] - current_minimum);
        current_minimum = Math.min(current_minimum, nums[i]);
    }

    return answer > 0 ? answer : -1;
};