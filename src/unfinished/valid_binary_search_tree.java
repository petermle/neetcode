package unfinished;
import java.util.LinkedList;
import java.util.Queue;

public class valid_binary_search_tree {
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

    public static boolean isValid(TreeNode root)
    {
        // bfs for equal chance of finding invalid patterns
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);

        while (!q.isEmpty())
        {
            TreeNode current = q.poll();
            if (current.left != null)
            {
                System.out.println("Correct statement: " + current.left.val + " < " + current.val);
                if (current.left.val > current.val)
                    return false;
                q.add(current.left);
            }

            if (current.right != null)
            {
                System.out.println("Correct statement: " + current.right.val + " > " + current.val);
                if (current.right.val < current.val)
                    return false;
                q.add(current.right);
            }
        }

        return true;
    }

    public static void main(String[] args)
    {
        // valid tree
        TreeNode validTree = new TreeNode(8,
            new TreeNode(3,
                new TreeNode(1),
                new TreeNode(6,
                    new TreeNode(4),
                    new TreeNode(7)
                )
            ),
            new TreeNode(10,
                null,
                new TreeNode(14,
                    new TreeNode(13),
                    null
                )
            )
        );

        // invalid tree
        TreeNode invalidTree = new TreeNode(5,
            new TreeNode(3,
                null,
                new TreeNode(6)
            ),
            new TreeNode(7)
        );

        System.out.println(isValid(validTree));
        System.out.println(isValid(invalidTree));
    }
}
