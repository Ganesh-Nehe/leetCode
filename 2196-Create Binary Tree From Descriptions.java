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
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodeMap = new HashMap<>();
        Set<Integer> children = new HashSet<>(); 
        for (int[] description : descriptions) {
            int parentVal = description[0];
            int childVal = description[1];
            boolean isLeft = description[2] == 1;
            nodeMap.putIfAbsent(parentVal, new TreeNode(parentVal));
            nodeMap.putIfAbsent(childVal, new TreeNode(childVal));
            TreeNode parentNode = nodeMap.get(parentVal);
            TreeNode childNode = nodeMap.get(childVal);
            if (isLeft) {
                parentNode.left = childNode;
            } else {
                parentNode.right = childNode;
            }
            children.add(childVal);
        }
        TreeNode root = null;
        for (int val : nodeMap.keySet()) {
            if (!children.contains(val)) {
                root = nodeMap.get(val);
                break;
            }
        }
        return root;
    }
}