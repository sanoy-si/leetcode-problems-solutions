class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def func(ind, total, combination):
            if target <= total or ind >= len(candidates):
                if target == total:
                    combinations.append(combination[:])
                
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i - 1] == candidates[i]:
                    continue

                combination.append(candidates[i])
                func(i + 1, total + candidates[i], combination[:])
                combination.pop()

        for i in range(len(candidates)):
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue

            func(i + 1, candidates[i], [candidates[i]])

        return combinations