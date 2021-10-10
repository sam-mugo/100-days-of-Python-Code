class Solution:
        # def twoSum(self, nums: List[int], target: int) -> List[int]:
        def twoSum(nums, target):
            checked = {}
            for k,v in enumerate(nums):
                othervalue = target - nums[k]
                print(f'k = {k} v = {v} and other value = {othervalue}')
                if othervalue in checked: 
                    return [k, checked[othervalue]]
                else: 
                    checked[v] = k
        nums = [2,3,4,6]
        target = 5
        print(twoSum(nums, target))
