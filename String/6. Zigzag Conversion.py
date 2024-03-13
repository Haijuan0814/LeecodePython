""" The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR" """

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zigzag = ['' for _ in range(numRows)]

        step = numRows + numRows - 2 
        n = len(s)
        word = ''
        for i in range(numRows):
            if i==0 or i == numRows-1:
                for j in range(i,n,step):
                    word += s[j]
            else:
                for j in range(i,n,step):
                    word += s[j]
                    mid = j + step - 2*i 
                    if mid < n:
                        word += s[mid]
        return word
        

