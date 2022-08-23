#include <stdio.h>

int main(){
	
	float x;
	float y;
	char ans;
	
	while (true){	
		printf("\nx의 값을 입력하시오:");
		scanf("%f", &x);
	
		if (x<=0){
			y = x*x - 9*x +2;
		}
		else{
			y = 7*x +2;
		}
	
		printf("f(x)의 값은 %f\n", y);
		
		
		printf("계속 계산을 진행할까요?");
		scanf("%c", &ans);
		
		if (ans == 'y'){
			continue;
		}
		else{
			break;
		}
		
	}

}
