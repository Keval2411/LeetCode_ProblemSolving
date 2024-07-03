/* Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
  */

var Issubsequence = function(s,t) {
    let sp=0,tp=0;
    l1 = s.length;
    l2 = t.length;

    while(sp<l1 && tp<l2){
        if (s[sp] === t[tp]){
            sp++
        }
        tp++
    }
    return sp === l1;
    
}
let s='abd'
let t='ahbkcd'
console.log(Issubsequence(s,t))