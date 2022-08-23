#include <stdio.h>

int main(){
	
	int num;

	printf("Enter a number : ");
	scanf("%d", &num);

	for(int i=1; i<num+1; i++){
		if(i/10 == 0 && i%3 == 0 && i%10 != 0){  //한자릿수 
			printf("* ");
		}
		else if(i/10 != 0 && (i%10)%3 == 0 && (i/10)%3 == 0 && i%10 != 0){  //둘 다 369인 두자릿수 
			printf("** ");			
		}
		else if(i/10 != 0 && i%10 != 0 && (i%10)%3 == 0 || (i/10)%3 == 0){  //하나만 369인 두자릿수 
			printf("* ");		
		}
		else{
			printf("%d ", i);
		}
	}
	
}
