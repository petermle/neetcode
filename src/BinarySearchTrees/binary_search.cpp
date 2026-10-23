#include <iostream>
#include <vector>

using namespace std;

// iterative array implementation
int search(vector<int>& nums, int target) 
{
    int l = 0;
    int r = nums.size();
    int mid = (l + r) / 2;

    while (l < r)
    {
        if (target < nums[mid])
            r = mid;
        else if (nums[mid] < target)
            l = mid + 1;
        else
            return mid;
        
        mid = (l + r) / 2;
    }

    return -1;
}

int main()
{
    vector<int> arr = {-1, 0, 2, 4, 6, 8};
    int target1 = 4;
    int expected1 = 3;

    int target2 = 3;
    int expected2 = -1;

    int output1 = search(arr, 4);
    int output2 = search(arr, 3);

    if (output1 != expected1)
    {
        cout << "Test case failed." << endl
            << "Expected: " << expected1 << endl
            << "Actual: " << output1 << endl;
    }

    if (output2 != expected2)
    {
        cout << "Test case failed." << endl
            << "Expected: " << expected2 << endl
            << "Actual: " << output2 << endl;
    }
}