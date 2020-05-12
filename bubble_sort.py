def bubble_sort(nums):
    for i in range(len(nums)):
        print(i)
        for j in range(0,len(nums)-(i+1)):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


nums=[4,3,1,2,7,9,8,6,5,0]
print(bubble_sort(nums))