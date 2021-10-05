def twoSum(self, nums, target):
        cache = {}
        
        for i in range(len(nums)):
            a = nums[i]
			#checks if the number is one of the needed ones
            if nums[i] in cache:
				#if it is then that is the solution
                return [cache[nums[i]], i]
			#if it is not we add the new one to the cache
            cache[target - a] = i