package Arrays;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class subarrays_distinct_element_sum_of_squares_1
{
    public static int sumCounts(List<Integer> nums)
    {
        int result = 0;

        int length = nums.size();
        for (int i = 0; i < length; ++i)
        {
            for (int j = 1; j < length - i + 1; ++j)
            {
                Set<Integer> temp = new HashSet<>(nums.subList(i, i + j));
                int tempSize = temp.size();
                result += tempSize * tempSize;
            }
        }

        return result;
    }

    public static void main(String[] args)
    {
        List<Integer> test = List.of(1, 2, 1);
        int output = sumCounts(test);
        int expected = 15;

        if (output != expected)
        {
            System.out.println("Test failed.");
            System.out.println("Output: " + output);
            System.out.println("Expected: " + expected);
        }
    }
}