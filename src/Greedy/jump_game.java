public class jump_game
{
    public static boolean canJump(int[] nums)
    {
        int len = nums.length;
        if (len == 0)
            return false;
        if (len == 1)
            return true;

        int farthest = nums[0];
        for (int i = 1; i < len; ++i)
        {
            if (i > farthest)
                return false;

            int currentFarthest = i + nums[i];
            if (currentFarthest > farthest)
                farthest = currentFarthest;

            if (farthest >= len - 1)
                return true;
        }
        return false;
    }

    public static void main(String[] args)
    {
        int[] test_1 = {2, 3, 1, 1, 4};
        int[] test_2 = {3, 2, 1, 0, 4};
        boolean test_1_expected = true;
        boolean test_2_expected = false;

        if (test_1_expected != canJump(test_1))
        {
            System.out.println("Test 1 failed.");
        }

        if (test_2_expected != canJump(test_2))
        {
            System.out.println("Test 2 failed.");
        }
    }
}