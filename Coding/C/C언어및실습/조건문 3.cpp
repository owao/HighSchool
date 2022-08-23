#include <stdio.h>

int main(){
	
	int price;
	int number;
	int money;
	
	int total_price;
	int need_money;
	
	scanf("%d %d %d", &price, &number, &money);
	
	total_price = price * number;
	need_money = total_price - money;
	
	if (need_money>0){
		printf("%d", need_money);
	}
	else{
		printf("0");
	}
	
}

