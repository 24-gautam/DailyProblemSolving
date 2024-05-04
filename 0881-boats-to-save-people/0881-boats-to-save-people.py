class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        i , j , boats = 0 , len(people) - 1 , 0

        while i <= j : 
            weight , j = people[j] , j - 1
            while i <= j and weight + people[j] <= limit : j , weight = j - 1 , weight + people[j] 
            while i <= j and weight + people[i] <= limit : i , weight = i + 1 , weight + people[i] 
            boats += 1

        return boats 
