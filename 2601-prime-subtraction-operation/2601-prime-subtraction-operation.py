class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime = self.sieve(max(nums))
        i = 0
        
        while i < len(nums):
            j = self.search(prime, nums[i])
            while j >= 0 and nums[i] - prime[j] <= (nums[i-1] if i > 0 else 0):
                j -= 1
            if j >= 0:
                nums[i] -= prime[j]
            elif i > 0 and nums[i] <= nums[i-1]:
                return False
            i += 1
        
        return True


    def sieve(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    
    def search(self, arr, target):
        left, right = 0, len(arr) - 1
        closest_less = -1  
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                closest_less = mid
                left = mid + 1  
            else:
                right = mid - 1 
        
        return closest_less 
