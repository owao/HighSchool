#include <stdio.h>

int main(){
	
	int month;
	
	scanf("%d", &month);
	
	if (month == 1 or month==2 or month==12)
		printf("겨울");
	if (month == 3 or month == 4 or month==5)
		printf("봄");
	if (month==6 or month==7 or month==8)
		printf("여름");
	if (month==9 || month==10 || month==11)
		printf("가을");
}
