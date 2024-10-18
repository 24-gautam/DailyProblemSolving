class Solution:
    def maximumSwap(self, num: int) -> int:
        d = [int(digit) for digit in str(num)]

        for i in range(len(d)) : 
            swap , k = False , i
            for j in range(i + 1 , len(d)) : 
                if d[i] < d[j] and d[j] >= d[k]: 
                    swap , k = True , j

            if swap : 
                d[i] , d[k] = d[k] , d[i] 
                break  
        
        return int(''.join(map(str , d)))

