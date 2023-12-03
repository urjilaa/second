class Solution:
    def average(self, salary: List[int]) -> float:
        salary=sorted(salary)
        tot=sum(salary[1:-1])
        div=len(salary[1:-1])
        ans=tot/div
        return ans