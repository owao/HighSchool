// ���ھ��� 1~30���� ���� �ִ� �� �߿��� 5�� �����Ͽ� ����ϱ� ( �ߺ����� )
package project1;

public class Ex01 {
	public static void main(String[] args) {
		int[] ballList = new int[5];
		int randomNum = 0;
		boolean insertYn = true;
		int i = 0;
		while( i < ballList.length ) {
			randomNum = (int) (Math.random() * 30) + 1;
			insertYn = true;
			for(int j=0; j<i; j++) {
				if ( ballList[j] == randomNum ) {
					insertYn = false;
					break;
				}
			}
			if ( insertYn )
			{
				ballList[i] = randomNum;
				i++;
			}
		}
		
		for(int ballNum : ballList)
			System.out.print(ballNum + " ");
	}
}
