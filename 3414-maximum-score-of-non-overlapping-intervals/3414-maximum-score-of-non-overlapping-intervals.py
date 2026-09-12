class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        arr = []
        for i, (start, end, weight) in enumerate(intervals):
            arr.append((end, start, weight, i))

        arr.sort()

        ends = [x[0] for x in arr]
        import bisect
        prev = []
        for i in range(n):
            start = arr[i][1]

            j = bisect.bisect_left(ends, start) - 1
            prev.append(j)

        dp = [[(0, []) for _ in range(n+1)] for _ in range(5)]
        take = [[False] * (n+1) for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n+1):
                end, start, weight, idx = arr[i-1]

                p = prev[i-1] + 1
                prev_score, prev_list = dp[k-1][p]
                candidate = (prev_score + weight, sorted(prev_list + [idx]))
                skip = dp[k][i-1]

                def better(a, b):
                    if a[0] != b[0]:
                        return a[0]>b[0]
                    return a[1]<b[1]
                if better(candidate, skip):
                    dp[k][i] = candidate
                    take[k][i] = True
                else:
                    dp[k][i] = skip
                    take[k][i] = False
                # dp[k][i] = max(skip, candidate, key=lambda x: (x[0], [-v for v in x[1]]))

                # if candidate > dp[k][i]:
                #     dp[k][i] = candidate
                #     take[k][i] = True

        ans = []
        k = 4
        i = n

        while i > 0 and k > 0:
            if take[k][i]:
                interval = arr[i-1]
                original_idx = interval[3]

                ans.append(original_idx)

                i = prev[i-1] + 1
                k -= 1
            else:
                i -= 1
        ans.sort()
        return ans