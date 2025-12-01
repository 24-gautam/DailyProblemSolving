class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        ans = -math.inf
        for j in range(k):
            sum = 0
            for i in range(j, len(prefix_sum) - k, k):
                sum = max(
                    prefix_sum[i + k] - prefix_sum[i],
                    sum + prefix_sum[i + k] - prefix_sum[i]
                )
                ans = max(ans, sum)

        return ans