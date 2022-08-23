// 인기 있는 과일 종류와 그 종류 개수 구하기 
package project1;

public class Ex03 {

	public static void main(String[] args) {
		String[] foods = {"딸기","사과","수박","수박","참외","메론","수박","참외","참외","사과","수박"};
		int length = foods.length;
		int equalCount = 0;
		int index = 0;
		String[] likeFood = new String[length];

		for(int i =0; i < length; i++)
			likeFood[i] = "";

		for(String food : foods) {
			equalCount = 0;
			for(int i =0; i < length; i++) {
				if ( likeFood[i].equals(food)) {
					equalCount++;
				}
			}
			if ( equalCount == 0 ) {
				likeFood[index] = food;
				index++;
			}
		}
		
		System.out.print("과일 종류 : ");
		for(String food : likeFood) {
			if ( food != "" )
				System.out.print( food + " " );
		}
		System.out.println("\n과일 종류 개수 : " + index);
	}

}
