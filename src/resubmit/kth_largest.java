import java.util.Arrays;
import java.util.HashMap;

public class kth_largest {
    private static int partition(int[] nums, int left, int right)
    {
        int pivot = nums[right];
        int i = left - 1;

        for (int j = left; j < nums.length - 1; ++j)
        {
            if (nums[j] < pivot)
            {
                ++i;
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }

        int temp = nums[i + 1];
        nums[i + 1] = nums[right];
        nums[right] = temp;

        return i + 1;
    }

    private static int quickSelect(int[] nums, int left, int right, int k)
    {
        int pivot = partition(nums, left, right);

        if (pivot > nums.length - k)      // target < pivot -> recurse the left side to find target
            return quickSelect(nums, left, pivot - 1, k);
        else if (pivot < nums.length - k) // pivot < target -> recurse the right side to find target
            return quickSelect(nums, pivot + 1, right, k);
        else                              // kth largest found
        {
            return nums[pivot];
        }
    }

    public static int findKthLargest(int[] nums, int k) 
    {
        return quickSelect(nums, 0, nums.length - 1, k);
    }

    public static void main(String[] args) 
    {
        HashMap<int[], Integer> testCases = new HashMap<>();
        int[] testCase_1 = {10, 7, 8, 9, 1, 5};
        int[] testCase_2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
        testCases.put(testCase_1, 9); // testCase: expected
        testCases.put(testCase_2, 5);
        for (int[] test : testCases.keySet())
        {
            String stringRepr = Arrays.toString(test);
            int expected = testCases.get(test);
            int result = findKthLargest(test.clone(), 2);

            if (result != testCases.get(test)) 
            {
                System.out.println("Test Case: '" + stringRepr + "' failed.");
                System.out.println("Expected: " + expected);
                System.out.println("Actual: " + result);
            }
            else
            {
                System.out.println("Test Case: '" + stringRepr + "' success.");
            }
        }   
    }
}
