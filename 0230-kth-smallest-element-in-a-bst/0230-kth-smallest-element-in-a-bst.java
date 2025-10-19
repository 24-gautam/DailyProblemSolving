/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res = -1 , i ;

    public int kthSmallest(TreeNode root, int k) {
        inOrder(root , k) ;
        return res ;
    }

    public void inOrder(TreeNode root , int k) {
        if(root != null) {
            inOrder(root.left , k) ;
            i++ ;
            if(i == k) res = root.val ;
            inOrder(root.right , k) ;
        }
    }
}