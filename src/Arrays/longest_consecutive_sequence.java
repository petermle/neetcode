package Arrays;

import java.util.Set;
import java.util.HashSet;

public class longest_consecutive_sequence 
{
    public static int longestConsecutive(int[] nums) 
    {
        // base case
        if (nums.length <= 1)
            return nums.length;
        
        // create num set
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums)
            numSet.add(num);

        int longest_sequence = 0;
        for (int num : nums)
        {
            int current = num;
            int current_sequence = 1;
            // only search when its the start of a newly discovered sequence; avoids recalculation [O(N^2)]
            while (!numSet.contains(num - 1))
            {
                // search forward until sequence ends
                if (numSet.contains(current + 1))
                {
                    current += 1;
                    current_sequence += 1;
                }
                else
                    break;
            }

            longest_sequence = longest_sequence < current_sequence ? current_sequence : longest_sequence;
        }
        return longest_sequence;
    }

    public static void main(String[] args)
    {
        int[] test = {0, 3, 2, 5, 4, 6, 1, 1};
        int output = longestConsecutive(test);
        int expected = 7;

        if (output != expected)
        {
            System.out.println("Test failed.");
            System.out.println("Expected: " + expected);
            System.out.println("Actual: " + output);
        }
    }
}
