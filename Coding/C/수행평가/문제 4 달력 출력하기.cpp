#include <stdio.h>

int main(){
	
	int year;
	int month;
	int day;
	int dow;
	int name;
	 
	
	printf("Enter year :");
	scanf("%d", &year);
	printf("Enter month :");
	scanf("%d", &month);
	printf("Enter day :");
	scanf("%d", &day);
	printf("Enter day of week :");
	scanf("%d", &dow);
	
	if (dow==0)
		printf("--> %d/%d/%d Sunday", year, month, day);
	if (dow==1)
		printf("--> %d/%d/%d Monday", year, month, day);
	if (dow==2)
		printf("--> %d/%d/%d Tuesday", year, month, day);
	if (dow==3)
		printf("--> %d/%d/%d Wensday", year, month, day);
	if (dow==4)
		printf("--> %d/%d/%d Tursday", year, month, day);
	if (dow==5)
		printf("--> %d/%d/%d Friday", year, month, day);
	if (dow==6)
		printf("--> %d/%d/%d Saturday", year, month, day);
		
}
