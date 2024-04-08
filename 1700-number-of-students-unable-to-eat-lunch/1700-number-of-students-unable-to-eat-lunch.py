class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dic , freq = [0] * 2 , [0] * 2 

        for i in students : dic[i] += 1 

        for i in range(len(students)) : 
            freq[sandwiches[i]] += 1 
            if freq[sandwiches[i]] > dic[sandwiches[i]] : return len(students) - i 
        
        return 0 