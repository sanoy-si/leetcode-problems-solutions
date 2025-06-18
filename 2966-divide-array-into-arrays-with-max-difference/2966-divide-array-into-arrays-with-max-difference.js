/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */

var divideArray = function(nums, k) {

    check = (answer) => {
        for (row of answer){
            if (row[row.length - 1] - row[0] > k){
                return false;
            }
        }

        return true;
    } 

    if (nums.length < 3 || nums.length % 3 != 0){
        return [];
    }

    nums.sort((a, b) => a - b);
    let answer = [];
    for (let i = 0; i < nums.length; i += 3){
        answer.push(nums.slice(i, i + 3));
    }
    return check(answer) ? answer : [];
};