# Programming Assignment 3

**UFIDS**:  
Karla Tran: 89625286  
Daniel Park: 75200264  

# Overview
This assignment uses a Python impelementation to find the Highest Value Longest Common Sequence (HVLCS) required in Programming Assignment 3.

# Questions
## Question 1

## Question 2
_Give a recurrence that is the basis of a dynamic programming algorithm to compute the
HVLCS of strings A and B. You must provide the appropriate base cases, and explain why
your recurrence is correct._

**Recurrence Equation**:  

$$
\text{OPT}(i, j) =
\begin{cases}
0 & \text{if } i = 0 \\
0 & \text{if } j = 0 \\
\max\big(\text{OPT}(i-1, j),\ \text{OPT}(i, j-1),\ v(a_i) + \text{OPT}(i-1, j-1) \text{ if } a_i = b_j\big) & \text{otherwise}
\end{cases}
$$

where:
- a, b = input strings
- i = indices in string a
- j = indices in string b
- v($a_i$) = value of character at i

**Explanation**:  
The base cases in this problem are the first two lines in the recurrence equation. In the cases that there are not enough characters in either string, there cannot be any matches in characters anymore; thus, the value would be 0.  
As for the last line, this line covers the dynamic programming logic where 3 potential cases can occur:  
1. The current character in strings differs ($a_i \neq b_j$), so the optimal solution excludes the current character.
  - The next potential character in the the solution is in the following characters in string a. Thus, there needs to be recursion on the next character in string `a` through the subproblem `OPT(i-1, j)` to uncover this character.
  - The next potential character in the solution is in the following characters in string b. Thus, there needs to be recursion on the next character in string `b` through the subproblem `OPT(i, j-1)` to uncover this character.
2. The current character in the strings match. (Thus, the condition $a_i = b_j$.) In this case, this character is potentially part of the highest value sequence, so this value is stored and added to solution of the subproblem `OPT(i-1, j-1)`. The other choices are still considered in the characters matching case as potential better solutions may exclude this character, so indepedent recursion for each individual string is continued.

As such, this recurrence captures all potential possibilities, allowing for an optimal solution to be found.

## Question 3
