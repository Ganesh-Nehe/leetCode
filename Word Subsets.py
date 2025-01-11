class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Create the max frequency dictionary for words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                max_freq[char] = max(max_freq[char], count)
        
        # Step 2: Filter words1 based on the max frequency dictionary
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result        