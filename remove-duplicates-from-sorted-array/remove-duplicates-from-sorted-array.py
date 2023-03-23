class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new=0
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                nums[new]=nums[i]
                new=new+1
        return new
            
        