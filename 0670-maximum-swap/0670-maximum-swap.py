class Solution:
    def maximumSwap(self, num: int) -> int:
        nums_list = list(str(num))
        changed = False
        for i in range(len(nums_list)):
            if changed:
                break
            
            max_ = i
            for j in range(len(nums_list) - 1, i, -1):
                if nums_list[max_] < nums_list[j]:
                    max_ = j
                    changed = True

            nums_list[i], nums_list[max_] = nums_list[max_], nums_list[i]

        return int("".join(nums_list))