#include <stdio.h>

int main(){
	
	int a, b, c;
	int money;
	
	scanf("%d %d %d", &a, &b, &c);
	
	if (a==b==c){
		money = 10000 + a*1000;
	}
	else if (a==b || a==c){
		money = 1000 + a*100;
	}
	else if (b==c){
		money = 1000 + b*100;
	}
	else{
		if (a>b && a>c){
			money = a*100;
		}
		else if (b>a && b>c){
			money = b*100;
		}
		else{
			money = c*100;
		}
	}
	
	printf("%d", money);
}
