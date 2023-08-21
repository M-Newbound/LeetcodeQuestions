class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # will be O(n) space
        frequencies = dict()

        # total iteration = O(n) time
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1               # O(1) time for hashmap lookup
        
        frequencies = sorted(frequencies.items(), key=lambda x: x[1])    # O(nlogn) time to sort
        return map(lambda x : x[0], frequencies[-k:])                    # O(k) time to splice + O(k) time to map

#    
#    This solution uses a dictionary (hashmap) to count the occurences of numbers
#    We then sort these occurences by the number of times they occur
#    Then we splice the uppermost k elements of this list, and return only their number
#
#    SPACE O(n)
#    TIME  O(nlogn) + O(k)
