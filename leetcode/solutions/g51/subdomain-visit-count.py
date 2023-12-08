class Solution:
    def subdomainVisits(self, cpdomains):
        counts  = {}
        ans = []
        for domain in cpdomains:
            count, subdomain = domain.split()
            count = int(count)
            sd = subdomain.split(".")
            for i in range(len(sd) - 1, - 1, - 1):
                curr_subdomain = ".".join(sd[i:])
                if curr_subdomain in counts:
                    counts[curr_subdomain] += count
                else:
                    counts[curr_subdomain] = count
        for a_domain in counts:
            ans.append(str(counts[a_domain]) + " " + a_domain )
        return ans




        