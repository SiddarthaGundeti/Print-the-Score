# Print-the-Score

Input: 120

Output: 620

Logical Approach:

Read Input:
Read the distance D (in km).

Initialize Score:
Initialize a variable score to 0.

Calculate Score for Each Tier:
For the first 50 km: 
If D > 50, add 50 * 3 to the score and subtract 50 from D.
If D <= 50, add D * 3 to the score and set D to 0.

For the next 50 km (51 - 100 km):
If D > 50, add 50 * 5 to the score and subtract 50 from D.
If D <= 50, add D * 5 to the score and set D to 0.
For the next 100 km (101 - 200 km):
If D > 100, add 100 * 6 to the score and subtract 100 from D.
If D <= 100, add D * 6 to the score and set D to 0.
For distances above 200 km:
Add D * 10 to the score.
 
Add Bonus Score:
Add the bonus score of 100 to score.

Output:
Print the total score.

Example for Clarity:

If the given distance D is 120 km:
For the first 50 km, the score is 50 * 3 = 150.
For the next 50 km (51 - 100 km), the score is 50 * 5 = 250.
For the remaining 20 km (101 - 120 km), the score is 20 * 6 = 120.
The bonus score is 100.
The total score is 150 + 250 + 120 + 100 = 620.
