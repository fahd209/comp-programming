import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        """
        understanding:
            given an array of nums  [10,9,1,1,1,2,3,1]
            the output should be a array sorted from least to greatest -> [1,1,1,1,2,3,9,10]

            the time complexity of the algorithm must be O(n log(n))

            approach:
                heapsort

                1. loop through the array & push each item to the heap
                2. pop from the heap and insert into an array\

            Time: O(nlog(n))
            Space: O(n)
        """

        heap = []
        res = []
        for n in nums:
            heapq.heappush(heap, n)

        while heap:
            res.append(heapq.heappop(heap))
        
        return res
        