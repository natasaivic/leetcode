# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
# of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


def moveZeros(nums):
    i = 0
    for j in range(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1



# Walk through: 

# i=0,j=0 nums=[0,1,0,15,9] nums[i]=0, nums[j]=0 -> j=j+1
# i=0,j=1 nums=[0,1,0,15,9] nums[j]!=0 -> swap(nums[i],nums[j]) -> i=i+1, j=j+1
# i=1,j=2 nums=[1,0,0,15,9] nums[j]=0 -> j=j+1
# i=1,j=3 nums=[1,0,0,15,9] nums[j]!=0 -> swap(nums[i],nums[j]) -> i=i+1, j=j+1
# i=2,j=4 nums=[1,15,0,0,9] nums[j]!=0 -> swapnums[i],nums[j]) -> i=i+1, j=4 was end array
# i=3,j=4 nums=[1,15,9,0,0] 
