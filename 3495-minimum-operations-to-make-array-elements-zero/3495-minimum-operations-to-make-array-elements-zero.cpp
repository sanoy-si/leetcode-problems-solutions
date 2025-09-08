class Solution {
public:

    long double ans_to_n(long long num, vector<long long> prefix){
        if (num == 0) return 0;
        int lg = floor(log(num) / log(4));
        long long answer = prefix[lg];
        answer += (num - pow(4, lg) + 1) * (lg + 1);

        return answer;
    }

    long long minOperations(vector<vector<int>>& queries) {
        vector <long long> prefix;
        prefix.push_back(0);
        for (int i = 1; i < 17; i++){ 
            prefix.push_back(prefix[i - 1] + (pow(4, i - 1) * 3) * i);
        }
        
        long long answer = 0;
        for (auto query : queries){
            long double all = ans_to_n(query[1], prefix), first = ans_to_n(query[0] - 1, prefix);
            answer += ceil((all - first) / 2);
        }

        return answer;
    }
};
