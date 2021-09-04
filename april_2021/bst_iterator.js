/*
 Time/Space Complexity = O(N)
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 */
 let stack = []
 var BSTIterator = function(root) {
     inorder(root)
 };
 
 /**
  * @return {number}
  */
 BSTIterator.prototype.next = function() {
     if (stack){
         const node = stack.pop()
         if (node.right){
             inorder(node.right)
         }
         return node.val
     }
     
 };
 
 /**
  * @return {boolean}
  */
 BSTIterator.prototype.hasNext = function() {
     return stack.length > 0
     
 };
 
 
 function inorder(node){
     while (node){
         stack.push(node)
         node = node.left
     }
 }