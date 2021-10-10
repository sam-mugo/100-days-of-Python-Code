class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(low,high,nums):
            if low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binSearch(mid+1,high,nums)
                else:
                    return binSearch(low,mid-1,nums)
            else:
                return -1
        return binSearch(0,len(nums)-1,nums)
