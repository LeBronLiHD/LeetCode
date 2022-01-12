#include <vector>
#define MIN(a, b) ((a > b) ? b : a)

template <class VECTOR>

class Solution
{
public:
    int maxArea(VECTOR &height)
    {
        // 2020.12.17 模电呵呵呵
        int contain;
        int i = 0, j = height.size() - 1;
        int len, hei;
        while (i < j)
        {
            len = (j - i);
            hei = MIN(height.at(i), height.at(j));
            contain = (contain > len * hei) ? contain : len * hei;
            if (height.at(i) == hei)
                i++;
            else
            {
                j--;
            }
        }
        return contain;
    }
    Solution() { Nothing = 0; }

private:
    int Nothing;
};