#include <stdio.h>

int main(){
	
	int month;
	
	scanf("%d", &month);
	
	if (month == 1 or month==2 or month==12)
		printf("�ܿ�");
	if (month == 3 or month == 4 or month==5)
		printf("��");
	if (month==6 or month==7 or month==8)
		printf("����");
	if (month==9 || month==10 || month==11)
		printf("����");
}
