class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res , stack = 0 , [target[0]]

        for i in range(1, len(target)) : 
            if stack[-1] > target[i] : 
                res += stack.pop() - target[i] 

            stack.append(target[i])

        return res + stack[-1]