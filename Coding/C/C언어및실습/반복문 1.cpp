#include <stdio.h>

int main(){
	
	int num;

	printf("Enter a number : ");
	scanf("%d", &num);

	for(int i=1; i<num+1; i++){
		if(i/10 == 0 && i%3 == 0 && i%10 != 0){  //���ڸ��� 
			printf("* ");
		}
		else if(i/10 != 0 && (i%10)%3 == 0 && (i/10)%3 == 0 && i%10 != 0){  //�� �� 369�� ���ڸ��� 
			printf("** ");			
		}
		else if(i/10 != 0 && i%10 != 0 && (i%10)%3 == 0 || (i/10)%3 == 0){  //�ϳ��� 369�� ���ڸ��� 
			printf("* ");		
		}
		else{
			printf("%d ", i);
		}
	}
	
}
