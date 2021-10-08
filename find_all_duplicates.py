"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
var findDuplicates = function(nums) {
    if (nums.length == 1){
        return []
    }
    
    let out = []
    for (let val of nums){
        if (nums[Math.abs(val) - 1] < 0){
            out.push(Math.abs(val))
        }
        else{
            nums[Math.abs(val) - 1] *= -1            
        }
    }    
    return out    
    
};