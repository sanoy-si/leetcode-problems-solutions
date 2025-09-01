class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        priority_queue<pair<double, int>> heap;
        int i = 0;
        for (auto cls: classes){
            int passing = cls[0];
            int total = cls[1];
            double current = (double)(passing) / total;
            double neww = (double)(passing + 1) / (total + 1); 
            heap.push({neww - current, i});
            i += 1;
        }

        for (int i = 0; i < extraStudents; i++){
            auto [diff, idx] = heap.top();
            heap.pop();
            classes[idx][0] += 1;
            classes[idx][1] += 1;
            int passing = classes[idx][0];
            int total = classes[idx][1];
            double current = (double)(passing) / total;
            double neww = (double)(passing + 1) / (total + 1); 
            heap.push({neww - current, idx});
        }

        long double total = 0;
        for (auto cls: classes){
            total += (double)(cls[0]) / cls[1];
        }

        return total / classes.size();
    }
};