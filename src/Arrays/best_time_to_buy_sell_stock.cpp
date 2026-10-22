#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int maxProfit(vector<int>& prices) 
{
    int lowest = numeric_limits<int>::max();
    int bestProfit = 0;

    for (size_t i = 0; i < prices.size(); ++i)
    {
        int current = prices[i];
        if (current < lowest)
        {
            lowest = current;
        }
        // no need for abs() bc current > lowest now
        else if (current - lowest > bestProfit)
        {
            bestProfit = current - lowest;
        }
    }

    return bestProfit;
}

int main()
{
    vector<int> testCase = {7, 1, 5, 3, 6, 4};
    int expected = 8;
    
    int output = maxProfit(testCase);
    if (expected != output)
        cout << "Test case failed.\n" 
            << "Expected: " << expected << '\n'
            << "Actual: " << output << endl;
    return 0;
}