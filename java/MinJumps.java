class MinJumps{

	public static int minJumps(int[] arr, int startIndex, int endIndex){

		if(startIndex == endIndex){
			return 0;
		}

		if(startIndex + arr[startIndex] >= endIndex){
			return 1;
		}


		int min = Integer.MAX_VALUE;
		for(int i=startIndex+1; i<endIndex && i<=startIndex+arr[startIndex]; i++){
			int a = 1;
			int b = minJumps(arr, i, endIndex);

			if(min>a+b){
				min = a+b;
			}
		}
		
		return min;

	}

	public static String split(){

		return "12---3     2015".split("[.\\-/\\s]+")[2];
	}

	public static void main(String[] args) {

		int[] arr = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9};
		System.out.print(split());
		
	}
}