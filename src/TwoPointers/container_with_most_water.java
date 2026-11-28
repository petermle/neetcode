package TwoPointers;

public class container_with_most_water {
    public static int maxArea(int[] heights)
    {
        if (heights.length <= 2) // constraints say length will be at min. 2
        {
            int minHeight = heights[0] <= heights[1] ? heights[0] : heights[1];
            return minHeight * minHeight;
        }

        int i = 0;
        int j = heights.length - 1;
        int maxValue = 0;
        while (i < j)
        {
            int distance = j - i;
            int minHeight = heights[i] <= heights[j] ? heights[i] : heights[j];
            int currentArea = distance * minHeight;

            if (currentArea > maxValue)
                maxValue = currentArea;

            if (heights[i] < heights[j])
                ++i;
            else if (heights[j] < heights[i])
                --j;
            else // they are the same; move either or
                ++i;
        }

        return maxValue;
    }

    public static void main(String[] args)
    {
        int[] testArray = {1, 7, 2, 5, 4, 7, 3, 6};
        int output = maxArea(testArray);
        int expected = 36;

        if (output != expected)
        {
            System.out.println("Test case failed.");
            System.out.println("Expected: " + expected);
            System.out.println("Actual: " + output);
        }
    }
}
