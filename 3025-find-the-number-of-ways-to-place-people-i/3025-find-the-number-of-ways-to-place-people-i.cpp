class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int answer = 0;
        for (int i = 0; i < points.size(); i++){
            for (int j = i + 1; j < points.size(); j++){
                auto x1 = points[i][0], y1 = points[i][1];
                auto x2 = points[j][0], y2 =  points[j][1];
                auto left = min(x1, x2), right = max(x1, x2);
                auto top = max(y1, y2), bottom = min(y1, y2);

                if (!((left == x1 && top == y1) || (left == x2 && top == y2))) {
                    continue;
                }
                bool valid = true;
                for (int k = 0; k < points.size(); k++){
                    if (k == i || k == j) continue;
                    if ((left <= points[k][0] && points[k][0] <= right) && (bottom <= points[k][1] && points[k][1] <= top)) {
                        valid = false; 
                        break;
                    }

                }
                if (valid) answer += 1;
            }
        }
        return answer;
    }
};