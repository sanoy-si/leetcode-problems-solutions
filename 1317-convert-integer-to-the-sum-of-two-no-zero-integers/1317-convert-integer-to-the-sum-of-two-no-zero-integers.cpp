class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        for (int i = 1; i <= n; i++){
            string str1 = to_string(i);
            string str2 = to_string(n - i);
            if (str1.find('0') == str1.npos && str2.find('0') == str2.npos)
                return {i, n - i};
        }

        return {0, 0};
    }
};