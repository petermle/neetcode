import java.util.HashSet;

public class happy_number {
    public static boolean isHappy(int n)
    {
        HashSet<Integer> seen = new HashSet<>();
        seen.add(n);
        int current = n;

        while (true)
        {
            int sum = 0;
            do
            {
                int digit = current % 10;
                sum += (digit * digit);  // avoiding Math.pow() for less overhead -> performance
                current /= 10;
            } while (current > 0);

            if (sum == 1)
                return true;
            else if (seen.contains(sum))  // loop detected
                return false;
            else
            {
                seen.add(sum);
                current = sum;
            }
        }
    }
    public static void main(String[] args)
    {
        int test_1 = 19;
        int test_2 = 2;
        boolean expected_1 = true;
        boolean expected_2 = false;

        if (isHappy(test_1) == expected_1)
        {
            System.out.println("Test Case 1 passed.");
        }
        if (isHappy(test_2) == expected_2)
        {
            System.out.println("Test Case 2 passed.");
        }
    }
}
