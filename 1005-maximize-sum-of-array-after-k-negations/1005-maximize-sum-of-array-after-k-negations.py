class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        flag=0
        c=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0:
                c+=1
                flag=1
                
        if flag==0:
            if k%2==0:
                return sum(nums)
            else:
                nums[0]=-nums[0]
                return sum(nums)
        else:
            if k>c:
                if (k-c)%2==0:
                    nums=[abs(i) for i in nums]
                    return sum(nums)
                else:
                    print('here')
                    nums=[abs(i) for i in nums]
                    nums.sort()
                    nums[0]=-nums[0]
                    return sum(nums)
            else:
                for i in range(len(nums)):
                    if nums[i]<0 and k!=0:
                        nums[i]=-nums[i]
                        k-=1
                
                        
                return sum(nums)
                        
                