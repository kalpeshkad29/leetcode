from collections import defaultdict

class Solution:
    def distance(self, nums):
        pos = defaultdict(list)

        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = [0] * len(nums)

        for indices in pos.values():

            m = len(indices)

            prefix = [0] * (m + 1)

            for i in range(m):
                prefix[i + 1] = prefix[i] + indices[i]

            for k in range(m):

                left = indices[k] * k - prefix[k]

                right = (prefix[m] - prefix[k + 1]) - indices[k] * (m - k - 1)

                ans[indices[k]] = left + right

        return ans