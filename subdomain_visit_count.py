"""
Time/Space complexity = O(N*M) here N is the max subdomains, M is number of domains
"""

from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        out = []
        if not cpdomains:
            return out
        
        domain_dict = defaultdict(int)
        
        for val in cpdomains:
            freq, domain = val.split()
            domain_dict[domain] += int(freq)
            domains = domain.split('.')
            temp = ''
            for i in range(-1, len(domains)*-1, -1):
                if temp:
                    temp = '{}.{}'.format(domains[i], temp)
                else:
                    temp = domains[i]
                domain_dict[temp] += int(freq)
                
        return ['{} {}'.format(str(val), key) for key, val in domain_dict.items()]