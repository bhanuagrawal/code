/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;
*/

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
import java.util.*;

class TestClass {


    static long p(int start, int end, long[] arr, int k){


        long averageStart = 0;
        long averageEnd = 0;
        
        if(start+k-1 <=end){

            for(int i=start; i<start+k; i++){
                averageStart += arr[i];
            }

            averageStart = (long)Math.floor((float )averageStart/k);
            averageStart = averageStart%1000000007;

            for(int i=end; i>end-k; i--){
                averageEnd += arr[i];
            }

            averageEnd = (long)Math.floor((float )averageEnd/k);
            averageEnd = averageEnd%1000000007;

            long startbk = arr[start+k-1];
            long endBk = arr[end-k+1];
            arr[start+k-1] = averageStart;
            long a = averageStart * p(start+k-1, end, arr, k);
            a = a%1000000007;


            arr[start+k-1] = startbk;


            arr[end-k+1] = averageEnd;
            long b = averageEnd * p(start, end-k+1, arr, k);
            b = b%1000000007;
            arr[end-k+1] = endBk;

            if(a > b){
                return a;
            }
            else{
                return b;
            }

        }
        
        return 1;

    }
    public static void main(String args[] ) throws Exception {
        /* Sample code to perform I/O:
         * Use either of these methods for input

        //BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String name = br.readLine();                // Reading input from STDIN
        System.out.println("Hi, " + name + ".");    // Writing output to STDOUT

        //Scanner
        Scanner s = new Scanner(System.in);
        String name = s.nextLine();                 // Reading input from STDIN
        System.out.println("Hi, " + name + ".");    // Writing output to STDOUT

        */

        
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();

        long arr[] = new long[n];
        for(int i=0; i<n; i++){
            arr[i] = s.nextLong();
        }


        System.out.println(p(0, n-1, arr, k)); 

        
        
        // Write your code here

    }
}


/*
Average Product
Given an array of  integers. Now, you can perform the following operation on this array:
. Remove exactly  integers from the front of the array or back of the array and take the average of these integers.
. Insert the floor value of this average value obtained in the above step to the respective side of the array from where you removed the integers.
. Repeat the above operations in that order as many times as you want or till the time there are at least  integers in the array. 

Now, you have to find the maximum product of the floor of average values that you have obtained in each operation. Since the number could be very large output it modulo .

Note: Once you have decided a side (front-side or back-side of the array), you cannot switch it during all the performed operations.

Input Format

The first line of the input contains two space-separated integers  and , the total number of elements in the array and the number of elements to remove from the array in each operation.
The next line contains  space-separated integers representing the elements of the array.

Output Format

In the single line of output print the maximum product of the floor of average values modulo .

Constraints



Sample Input
6 3
5 4 -2 7 3 -1
Sample Output
8
Explanation
Note that, it is optimal to pick the elements from the front of the array.
Operation : 
Array becomes, 
Operation : 
Array becomes,  
Now, you cannot perform operations further.

Maximum product 
Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
Time Limit: 1.0 sec(s) for each input file
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes













City Tour
There are  cities numbered from  to  in BitLand, each of which has its own value .

You are travelling in BitLand. At first you choose a city assumed to be  and a number assumed to be . Then you can start your trip at the city numbered . After that you go to the one numbered , and then  and so on until you reach  again.

When you finish your journey, you add up the values of all the different cities where you have ever been to and regard the result as your degree of satisfaction. Your task is to select  and  wisely so that you can maximize your degree of satisfaction.

Input Format

The first line of the input contains an integer , denoting the number of cities in BitLand.
The next line contains  space-separated integers , denoting value of each city.

Output Format

In the single line of the output print the required maximum value.

Constraints



Sample Input
7
5 -7 1 4 -2 3 8
Sample Output
12
Explanation
Select the first city  and set  to be , this way you can travel all the cities. Note that there is no other way to get the value better than .

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
Time Limit: 1.0 sec(s) for each input file
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes
Allowed Languages: Java, Java 8









Restore the Sequence
Given a sequence of  distinct integers. In each step, a group of zero or more integers (not necessarily contiguous) change their positions. This process is repeated for  times. An integer  moves only once in all the  steps. The original sequence is restored at the beginning of each step.

Suppose the initial sequence is .

After step , let's say  moves. So, sequence after first step may be  or some other sequence is also possible e.g. .

After step , since  has already moved it will not move again. Let's say the group of  and  moves this time. So, the sequence may be  or .

After step , let's say no one moves. So, our sequence remains .

Similarly step  and step  can be processed.

Now, you are given the sequence of integers after each step. Can you restore the original sequence? It is guaranteed that the sequence exists and is unique.

Input Format

The first line of the input contains a single integer , the number of integers in the sequence.
Then  lines follow, the -th line contains  space-separated integers denoting the sequence after -th step.

Output Format

Output  space-separated integers representing the original sequence.

Constraints


Sample Input
6
2 3 1 6 4 7
2 1 6 3 4 7
7 4 2 3 6 1
2 3 6 1 4 7
3 6 1 4 2 7 
Sample Output
2 3 6 1 4 7
Explanation
The original sequence is . The movements are as follows:

 :  moves

 :  and  moves

 :  and  moves

 : no movement

 :  moves

*/