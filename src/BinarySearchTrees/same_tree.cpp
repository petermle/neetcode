#include <iostream>
#include <queue>
#include <utility>

using namespace std;

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right): 
        val(x), left(left), right(right) {}
};

bool isSameTree(TreeNode* p, TreeNode* q)
{
    /*
    i was initially using 2 queues to keep track,
    but found the 'pair approach' to be cleaner and 
    more intuitive, given the problem context.

    time/space complexity remain the same.
    */
    queue<pair<TreeNode*, TreeNode*>> nodes;
    nodes.push({p, q});

    while (!nodes.empty())
    {
        auto current = nodes.front();
        nodes.pop();
        TreeNode* pCurrent = current.first;
        TreeNode* qCurrent = current.second;

        if (pCurrent == nullptr && qCurrent == nullptr)
        {
            continue;
        }
        else if (
            (pCurrent == nullptr && qCurrent != nullptr) ||
            (pCurrent != nullptr && qCurrent == nullptr))
        {
            return false;
        }
        else if (pCurrent->val != qCurrent->val)
        {
            return false;
        }
        else
        {
            nodes.push({pCurrent->left, qCurrent->left});
            nodes.push({pCurrent->right, qCurrent->right});
        }
    }

    return true;
}

int main()
{
    // testcase 1:
    // p = [1, 2, 3], q = [1, 2, 3]
    TreeNode* p1 = new TreeNode(1);
    p1->left = new TreeNode(2);
    p1->right = new TreeNode(3);

    TreeNode* q1 = new TreeNode(1);
    q1->left = new TreeNode(2);
    q1->right = new TreeNode(3);

    bool result1 = isSameTree(p1, q1);
    std::cout << "Example 1 result: " << boolalpha << result1 << endl;

    // testcase 2:
    // p = [1, 2], q = [1, null, 2]
    TreeNode* p2 = new TreeNode(1);
    p2->left = new TreeNode(2);

    TreeNode* q2 = new TreeNode(1);
    q2->right = new TreeNode(2);

    bool result2 = isSameTree(p2, q2);
    std::cout << "Example 2 result: " << result2 << endl;

    return 0;
}