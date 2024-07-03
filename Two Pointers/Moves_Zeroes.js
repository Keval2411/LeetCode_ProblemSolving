
/* Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]*/

var moveZeroes = function(nums) {
    let last_Nonezero = 0;
    s = nums.length

    for(let current=0;current<s;current++){
        if (nums[current] !== 0){
            [nums[current],nums[last_Nonezero]] = [nums[last_Nonezero], nums[current]]
            last_Nonezero++
        }
    }

    
};
let nums1 = [0,2,4,0,9,24,0]
moveZeroes(nums1)
console.log(nums1)