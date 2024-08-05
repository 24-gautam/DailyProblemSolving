class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(sorted([sum(nums[i:j+1]) for i in range(len(nums)) for j in range(i , len(nums))])[left - 1 : right]) % (1000000007)