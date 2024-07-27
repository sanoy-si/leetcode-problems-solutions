class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        for num in nums:
            prefix_product.append(prefix_product[-1] * num)
        
        postfix_product = [1]
        for i in range(len(nums)-1, -1, -1):
            postfix_product.append(postfix_product[-1] * nums[i])
        
        postfix_product = postfix_product[::-1]

        answer = []
        for i in range(len(nums)):
            left = prefix_product[i]
            right = postfix_product[i + 1]
            answer.append(left * right)
        

        return answer