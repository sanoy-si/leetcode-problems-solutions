class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idxs = defaultdict(list)
        for i in range(len(nums)):
            idxs[nums[i]].append(i)
        
        arr = [0 for i in range(len(nums))]

        for value in idxs.values():
            left_sum = 0
            right_sum = sum(value)

            for i in range(len(value)):
                arr[value[i]] = abs(left_sum - (i * value[i])) + abs(right_sum - ((len(value) - i) * value[i]))
                left_sum += value[i]
                right_sum -= value[i]
        
        return arr
