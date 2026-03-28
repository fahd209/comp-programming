class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        understanding:
            input: [100,4,200,1,3,2]
            output: 4
            why: [1, 2, 3, 4]

        approach:
            max: 1, 2, 3, 4 
            set: 
            array: [100,4,200,1,3,2]
         iterator:            i


        """

        sequence_set = set(nums)
        max_seq = 0

        for n in sequence_set:
            if not n - 1 in sequence_set:
                cur = n 
                count = 1
                while cur + 1 in sequence_set:
                    count += 1
                    cur = cur + 1
                max_seq = max(max_seq, count)


        return max_seq
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest_seq = 0

        # loop through each num and check if its a start of sequence
        for n in nums:
            if not n - 1 in nums_set:
                current_sequence = 1
                
                # keep incrementing the current_sequence counter until we break out the current sequence
                while n + current_sequence in nums_set:
                    current_sequence += 1
                longest_seq = max(longest_seq, current_sequence)

        return longest_seq


        