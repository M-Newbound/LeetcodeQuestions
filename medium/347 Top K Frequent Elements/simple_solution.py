class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = dict()

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        frequencies = sorted(frequencies.items(), key=lambda x: x[1])
        return map(lambda x : x[0], frequencies[-k:])
