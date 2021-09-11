/*
Time Complexity = O(N)
Space Complexity = log(N)
*/

var sortedArrayToBST = function(nums) {
    
    if (!nums.length){
        return null
    }
    
    const mid = Math.floor(nums.length / 2)
    let node = new TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums.slice(0, mid))
    node.right = sortedArrayToBST(nums.slice(mid + 1))
    return node  
};