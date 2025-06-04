Paul is given an array A of length N. He must perform the following Operations on the
array sequentially:
* Choose any two integers from the array and calculate their average.
* If an element is less than the average, update it to 0. However, if the element is
greater than or equal to the average, he need not update it.
Your task is to help Paul find and return an integer value, representing the minimum
possible sum of all the elements in the array by performing the above operations. Note: An exact average should be calculated, even if it results in a decimal.

Input Format:
input1: An integer value N, representing the size of the array A.
input2: An integer array A.
Output Format:
Return an integer value, representing the minimum possible sum of all the elements
in the array by
Sample Input
5
1 2 3 4 5
Sample Output
5
 
arr=list(map(int,input().split()))
arr.sort()
a1=arr[-1]
a2=arr[-2]
sum=0
avg=(a1+a2)/2
for i in range(len(arr)):
    if arr[i]<avg:
        arr[i]=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)
print(avg)

''The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
Output:

4

Explanation:
Total amount of food required for all rats = r * unit

= 7 * 2 = 14.

The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats. Thus, output is 4.


n=int(input())
r=int(input())
units=int(input())
arr=list(map(int,input().split()))
food_required=r*units
if(len(arr)==0):
    print(-1)
for i in range(n):
    food_required=food_required-arr[i]
    if(food_required<0):
        break
if (food_required>0):
    print(0)
print(abs(food_required))

You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0 





