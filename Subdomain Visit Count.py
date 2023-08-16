class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        d = defaultdict(int)
        for domain in cpdomains:
            count,subDomains = domain.split(' ')
            count = int(count)
            
            subDomains = subDomains.split('.')
            subDomain = subDomains[-1]
            d[subDomain] += count 
            
            for j in range(len(subDomains) -2, -1, -1):
                subDomain = subDomains[j] + '.' + subDomain
                d[subDomain] += count  
            ans = [str(j) + ' ' + i for i,j in d.items()]
        return ans
                
        
