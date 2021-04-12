/*
Time complexity = O(log N) average, O(N) for skewed tree
Space complexity = O(1)
*/

var inorderSuccessor = function(root, p) {
    
    if (root == null){return null}
    
    var successor = null
    
    while (root)
        {
            
            if (p.val >= root.val)
                {
                    root = root.right
                }
            
            else
            {
              successor = root
                root = root.left
            }
        }
    return successor
    