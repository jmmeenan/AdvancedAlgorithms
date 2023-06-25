/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    nums = nums.sort(function(a,b){return a-b});
    var i = 0;
    var j = nums.length - 1;
    while(i < j){
        if(nums[i] + nums[j] == target){
            return [i+1, j+1];
        }else if(nums[i] + nums[j] > target){
            j--;
        }else{
            i++;
        }
    }
};