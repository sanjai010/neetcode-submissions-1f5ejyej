class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        n=len(people)
        
        i=0
        j=n-1
        while i<=j:
            if people[i]+ people[j]<=limit:
                i+=1
                j-=1
                count+=1
            else:
                j-=1
                count+=1
        if i==j:
            count+=1
        return count
            

        