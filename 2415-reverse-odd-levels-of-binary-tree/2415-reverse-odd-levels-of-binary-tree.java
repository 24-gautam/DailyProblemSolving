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
    public TreeNode reverseOddLevels(TreeNode root) {
        int i = 0 ;
        Queue<TreeNode> ltr = new LinkedList() ; 
        Queue<Integer> rtl = new LinkedList() ; 

        ltr.add(root) ; rtl.add(root.val) ; 

        while(ltr.size() > 0) {
            var node = ltr.poll() ;
            if(node.left != null) {
                ltr.add(node.right) ; ltr.add(node.left) ; 
                rtl.add(node.right.val) ; rtl.add(node.left.val) ; 
            }
        }

        ltr.add(root) ; 

        while(ltr.size() > 0) {
            int n = ltr.size() ; 
            while(n-- > 0) {
                int x = rtl.poll() ;
                var node = ltr.poll() ; 

                if(i % 2 == 1) node.val = x ; 

                if(node.left != null) {
                    ltr.add(node.left) ; 
                    ltr.add(node.right) ;
                }
            }
            i++ ;
        }

        return root ;
    }
}