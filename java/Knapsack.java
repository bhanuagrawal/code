class Knapsack{

	static int max(int a, int b){ return a>b?a:b;}

	static int knapsack(int[] value, int[] weight, int w, int index){

		if(index<weight.length && w>0){
			int a = value[index]+knapsack(value, weight, w-weight[index], index+1);
			int b = knapsack(value, weight, w, index+1);
			System.out.println(Integer.toString(index) + " " +  Integer.toString(a) + " " + Integer.toString(b));
			if(w<weight[index]){
				return b;
			}

			

			return max(a, b);
		}


		return 0;
		
	}

	public static void main(String[] args) {
		
		int[] value = new int[]{60, 100, 120};
		int[] weight = new int[]{10, 20, 30};


		int w = 50;
		System.out.print(knapsack(value, weight, w, 0));
	}
}