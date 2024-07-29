func containsDuplicate(nums []int) bool {
    counter := map[int]int{}
    for _, v := range nums{
        counter[v] += 1
    }

    for _, v := range counter{
        if v > 1{
            return true
        }
    }

    return false 
}