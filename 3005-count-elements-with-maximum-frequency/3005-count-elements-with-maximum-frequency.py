class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic , maxFreq , maxFreqCnt = defaultdict(int) , 0 , 0
        for i in nums : 
            dic[i] += 1 
            if dic[i] > maxFreq : maxFreq , maxFreqCnt = dic[i] , 0 
            if dic[i] == maxFreq : maxFreqCnt += 1 

        return maxFreqCnt * maxFreq 