package BinarySearchTrees;
public class balanced_tree
{
    private static class TreeNode
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
    
    // in order
    public static void dfs(TreeNode root)
    {
        if (root == null)
        {
            return;
        }
        dfs(root.left);
        System.out.println(root.val);
        dfs(root.right);
    }

    public static int maxDepth(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return 1 + Math.max(left, right);
    }

    public static boolean isBalanced(TreeNode root)
    {
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return Math.abs(right - left) <= 1;
    }

    public static void main(String[] args)
    {
        TreeNode root = new TreeNode(
            3, 
            new TreeNode(9), new TreeNode(20, 
            new TreeNode(15), new TreeNode(7))
        );

        System.out.println(isBalanced(root));
    }    
}
