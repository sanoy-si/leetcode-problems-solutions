class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for domain in cpdomains:
            count, sub_domains = domain.split()
            count = int(count)
            sub_domains = sub_domains.split('.')
            for i in range(len(sub_domains)):
                sub_domain = '.'.join(sub_domains[i:])
                counter[sub_domain] += count
        
        answer = [f"{value} {key}" for key, value in counter.items()]
        return answer


        