#include <stdio.h>

int main(){
	
	int score;
	char grade;
	
	scanf("%d", &score);
	
	if (score<0 || score>100){
		printf("wrong score");
	}
	
	switch(score/10){
		case 10: case 9:
			grade = 'A';
			break;
		case 8:
			grade = 'B';
			break;
		case 7:
			grade = 'C';
			break;
		case 6:
			grade = 'D';
			break;
		default:
			grade = 'F';
			break;
	}
	
	printf("당신의 등급은 %c입니다.", grade);
	

}
