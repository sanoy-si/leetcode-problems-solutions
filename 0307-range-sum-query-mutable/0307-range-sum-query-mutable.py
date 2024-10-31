class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)
        self.build(0, self.n - 1, 0)
    
    def build(self, n_left, n_right, t_idx):
        if n_left == n_right:
            self.tree[t_idx] = self.nums[n_left]
            return self.tree[t_idx]
        
        mid = (n_right + n_left) // 2
        left_child = 2 * t_idx + 1
        right_child = 2 * t_idx + 2 

        self.tree[t_idx] = self.build(n_left, mid, left_child) + self.build(mid + 1, n_right, right_child)

        return self.tree[t_idx]
        


    def update(self, index: int, val: int) -> None:
        def dfs(n_left, n_right, index, t_index):
            if n_left == n_right == index:
                self.tree[t_index] = val
                return self.tree[n_left]
            
            mid = (n_left + n_right) // 2
            left_child = 2 * t_index + 1
            right_child = 2 * t_index + 2

            if index <= mid:
                dfs(n_left, mid, index, left_child)

            else:
                dfs(mid + 1, n_right, index, right_child)

            self.tree[t_index] = self.tree[left_child] + self.tree[right_child]
        
        dfs(0, self.n - 1, index, 0)        

    def sumRange(self, left: int, right: int) -> int:
        def dfs(left, right, n_left, n_right, t_index):
            if right < n_left or left > n_right:
                return 0
            
            if left <= n_left and right >= n_right:
                return self.tree[t_index]
            
            mid = (n_left + n_right) // 2
            left_child = 2 * t_index + 1
            right_child = 2 * t_index + 2

            return dfs(left, right, n_left, mid, left_child) + dfs(left, right, mid + 1, n_right, right_child)
        
        return dfs(left, right, 0, self.n - 1, 0)


            


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)