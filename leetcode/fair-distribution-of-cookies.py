class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_unfairness = float("inf")
        
        def func(distribution, ind):
            if ind == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(distribution))
                return
            
            for i in range(k):
                distribution[i] += cookies[ind]
                
                if distribution[i] <= self.min_unfairness:
                    func(distribution, ind + 1)

                distribution[i] -= cookies[ind]
        
        distribution = [0] * k

        func(distribution, 0)

        return self.min_unfairness

            



            

                



            

