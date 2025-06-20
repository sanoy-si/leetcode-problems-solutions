/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxDistance = function(s, k) {
    let e_count = w_count = n_count = s_count = 0;
    let answer = 0;
    for (char of s){
        if (char == "S")
            s_count += 1;
        else if (char == "W")
            w_count += 1;
        else if(char == "N")
            n_count += 1;
        else
            e_count += 1;

        let unchanged = Math.abs(s_count - n_count) + Math.abs(e_count - w_count);
        let max_change = Math.min(s_count, n_count) + Math.min(e_count, w_count);
        answer = Math.max(answer, unchanged + 2 * Math.min(k, max_change));
    }

    return answer;
};