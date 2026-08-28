package BinarySearchTrees;

public class delete_bst_node 
{
    private static TreeNode masterRoot;

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

    public static TreeNode deleteNode(TreeNode root, int key)
    {
        if (root == null)
        {
            return null;
        }
        if (root.val == key)
        {
            if (root.right != null)
            {
                return root.right;
            }
            else if (root.left != null)
            {
                return root.left;
            }
            
            TreeNode i = root;
            while (i.left != null)
                deleteNode(i.left, key);
            
            root.val = i.val;
            int temp = i.val;
            i.val = i.left.val;
            i.left.val = temp;

        }
        else if (root.val > key)
            root.left = deleteNode(root.left, key);
        else if (root.val < key)
            root.right = deleteNode(root.right, key);

        return root;
    }

    public static void main(String[] args)
    {
        TreeNode root = new TreeNode(5);

        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);

        TreeNode node3 = new TreeNode(1);
        TreeNode node4 = new TreeNode(4);

        root.left = node1; 
        root.right = node2;
        node1.left = node3; 
        node1.right = node4;

        masterRoot = deleteNode(root, 3);
        
        System.out.println("root: " + masterRoot.val);
        System.out.println("left: " + masterRoot.left.val);
    }   
}
