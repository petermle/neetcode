#include <iostream>
#include <vector>

using namespace std;

void sortColors(vector<int>& nums)
{
    const int COLOR_COUNT = 3;

    // represents [red, white, blue] in original problem
    int counts[COLOR_COUNT] = {0};

    // loop purely to count
    for (const int& num : nums)
        counts[num] += 1;

    // init. i outside so we can keep track of array through single pass
    int i = 0;

    // j = current color; [red, white, blue] in original problem
    for (int j = 0; j < COLOR_COUNT; ++j)
    {
        int count = counts[j];
        // k = number of current color present in 'nums'
        for (int k = 0; k < count; ++k)
        {
            // overwrite original array 'nums' sequentially and
            //     save index through loops with 'i'
            nums[i] = j;
            i += 1;
        }
    }
}

int main()
{
    vector<int> testCase = {2, 0, 2, 1, 1, 0};
    sortColors(testCase);
    
    for (const int& num : testCase)
    {
        cout << num << endl;
    }

    return 0;
}