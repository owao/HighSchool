// �α� �ִ� ���� ������ �� ���� ���� ���ϱ� 
package project1;

public class Ex03 {

	public static void main(String[] args) {
		String[] foods = {"����","���","����","����","����","�޷�","����","����","����","���","����"};
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
		
		System.out.print("���� ���� : ");
		for(String food : likeFood) {
			if ( food != "" )
				System.out.print( food + " " );
		}
		System.out.println("\n���� ���� ���� : " + index);
	}

}
