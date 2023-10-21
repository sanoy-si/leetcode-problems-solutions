class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tp=1
        ttp=1
        answer = []
        v=False
        o=False
        for i in nums:
            if i!=0:
                tp*=i
            elif v:o=True
            else:v=True
        if v:
            for i in nums:
                if  i == 0 and not o: answer.append(tp)
                else:answer.append(0)
        else:
            for i in nums:
                answer.append(tp//i)
        return answer
