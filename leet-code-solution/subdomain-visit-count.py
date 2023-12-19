class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = defaultdict(int)

        for cp in cpdomains:
            count, domain = cp.split()
            subdomain = domain.split('.')

            for i in range(len(subdomain)):
                newstr = '.'.join(subdomain[i:])
                domain_dict[newstr] += int(count)

        ans = [str(count) + " " + subdomain for subdomain, count in domain_dict.items()]
        #ans = []
        #for val in domain_dict:
        #    ans.append(str(domain_dict[val]) + " " + val)

        return ans