import utils.BSTMaker;

public class maximum_depth_of_binary_tree
{
    public static class TreeNode 
    {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) 
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static int maxDepth(TreeNode root)
    {
        // depth first search
        if (root == null)
            return 0;

        int left_depth = 0;
        int right_depth = 0;
        if (root.left != null)
            left_depth = maxDepth(root.left);
        if (root.right != null)
            right_depth = maxDepth(root.right);

        return 1 + ( (left_depth > right_depth) ? left_depth : right_depth );
    }

    public static void main(String[] args)
    {
        Integer[] treeArray = {
            1, 
            2, 3, 
            null, 4, 
            null, null, 
            5, null,
            null, 6,
            null, 7,
            8, null
        };

        BSTMaker.generateBST(treeArray);
        System.out.println(BSTMaker.root);
        // Level 7 (Deepest leaf)
        TreeNode node8 = new TreeNode(8);

        // Level 6
        TreeNode node7 = new TreeNode(7, node8, null); // 8 is left child of 7

        // Level 5
        TreeNode node6 = new TreeNode(6, null, node7); // 7 is right child of 6

        // Level 4
        TreeNode node5 = new TreeNode(5, null, node6); // 6 is right child of 5

        // Level 3
        TreeNode node4 = new TreeNode(4, node5, null); // 5 is left child of 4

        // Level 2
        TreeNode node2 = new TreeNode(2, null, node4); // 4 is right child of 2
        TreeNode node3 = new TreeNode(3);              // Simple leaf node at depth 2

        // Level 1 (Root)
        TreeNode root = new TreeNode(1, node2, node3);

        int result = maxDepth(root);
        System.out.println(result);
    }
} 