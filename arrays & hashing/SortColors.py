
# my solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # group colors
        color_group = defaultdict(list)
        for n in nums:
            color_group[n].append(n)
        
        # loop through each group and replace the elements in num with the elements in the group
        # print(color_group)
        index = 0
        for i in range(3):
            for n in color_group[i]:
                nums[index] = n
                index += 1


# neetcode
