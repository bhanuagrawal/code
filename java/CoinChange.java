class CoinChange {

	static int countWays(int[] coins, int m, int n){

		if(m==0){
			return 1;
		}

		if(m<0 || (m>0 && n==0) ){
			return 0;
		}

		System.out.println(m-coins[n-1]+", " + n + "   "+ m+ ", " + (n-1));
		return countWays(coins, m-coins[n-1], n) + countWays(coins, m, n-1);
	}

	static int countWaysDp(int[] coins, int m, int n){

		int[][] table = new int[m+1][n+1];


		for(int i=0; i<=n; i++){
			table[0][i] = 1;
		}

		for(int i=1; i<=m; i++){
			table[i][0] = 0;
		}


		for(int i=1; i<=n; i++){

			for(int j=1; j<=m; j++){

				if(j-coins[i-1]>=0){
					table[j][i] = table[j-coins[i-1]][i] + table[j][i-1];
				}
				else{
					table[j][i] = table[j][i-1];
				}
				
			}
		}


		return table[m][n];

	}

	public static void main(String[] args) {

		int coins[] = new int[]{1, 2, 3};
		int n = coins.length;

		int m = 4;
		System.out.print(countWaysDp(coins, m, n));
	}
}


Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)


min(solution that include ith element , do not contain ith element)
min(1, i) min(i, 9)