class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        understand:
            1. Given array: nums, and integer: k = 2
            2. return the 2 most frequent elements in the array

            will there be negative numbers?
            what if the array is empty?

            {
                1: 3,
                2: 2,
                3: 1
                4: 3
            }

            [0,[3],[2],[1, 4],0,0]

            approach: 
                1. count the accurences of the nums in a map
                2. initilize an array count that will have value of a num at the index that equal to the accurence of that number
                3. loop through the array backwards because the max freq element will to the right of the array
                4. if count[i] != 0 then I'll keep appending to my result array until result.length == k
        """

        accurence_count = {}
        count = [0] * (len(nums) + 1)
        result = []

        for n in nums:
            accurence_count[n] = accurence_count.get(n, 0) + 1

        for key in accurence_count:
            if count[accurence_count[key]] == 0:
                count[accurence_count[key]] = [key]
            else:
                count[accurence_count[key]].append(key)
        
        for i in range(len(count) - 1, -1, -1):

            if count[i] != 0:
                for n in count[i]:
                    if len(result) == k:
                        return result
                    result.append(n)

        return result
    

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_buckit = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, value in count.items():
            freq_buckit[value].append(key)

        res = []
        for i in range(len(freq_buckit) - 1, 0, -1):
            if freq_buckit[i] != []:
                for n in freq_buckit[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
            
        