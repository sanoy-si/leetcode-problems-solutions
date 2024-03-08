class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.vote_results = []
        scores = defaultdict(int)
        highest_vote = [0, -1]

        for i in range(len(times)):
            scores[persons[i]] += 1

            if scores[persons[i]] >= highest_vote[0]:
                
                highest_vote = [scores[persons[i]], persons[i]]
                self.vote_results.append((times[i], highest_vote[1]))


    def q(self, t: int) -> int:
        left, right = 0, len(self.vote_results) - 1

        ind = len(self.vote_results) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.vote_results[mid][0] <= t:
                ind = mid
                left = mid + 1
            
            else:
                right = mid - 1

        return self.vote_results[ind][1]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)