''' Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters. '''

class Solution:
    def maxVowels(self, s: str, k: int):
        n = len(s)
        current_count = 0;
        max_count = 0;
        vowels = 'a,e,i,o,u';
        
        for i in range(k):
            if s[i] in vowels:
                current_count += 1;
        max_count = current_count
        
        for i in range(k,n):
            if s[i-k] in vowels:
                current_count -= 1;
            if s[i] in vowels:
                current_count += 1;
            max_count = max(current_count,max_count)
            
        return max_count  
            
Solution = Solution()
print(Solution.maxVowels(s = 'abciiidef', k=3))
print(Solution.maxVowels(s = 'aeiou', k=2))
print(Solution.maxVowels(s = 'leetcode', k=3))
        