// �йи� ������� ����� ���α׷�
package project1;

import java.util.Calendar;
import java.util.Scanner;

public class Ex02 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Calendar now = Calendar.getInstance();
		int nowHour    = now.get(Calendar.HOUR);		// 0 ~ 11�� 
//		int nowHour    = now.get(Calendar.HOUR_OF_DAY);	// 0 ~ 23��
		int nowMinute = now.get(Calendar.MINUTE);
		int nowWeek    = now.get(Calendar.DAY_OF_WEEK);
		int totalCost = 0;
		int cost = 12000;
		int num = 0;
		
		System.out.println("�ο����� �Է��ϼ��� : ");
		num = sc.nextInt();
		sc.close();

		if ( nowWeek == 4 ) cost = 8000;
		else if (( nowHour == 10 && ( nowMinute >= 30 && nowMinute <= 59 ) ) || ( nowHour == 11 && nowMinute == 0 )) 
			cost *= 0.8;
		
		totalCost = cost * num ;
		System.out.println("�� �ݾ� = " + totalCost);
	}
}
