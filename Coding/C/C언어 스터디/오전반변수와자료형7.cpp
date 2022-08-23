#include <stdio.h>

int main(){
	
	const float mile = 0.621371;
	
	int km_1 = 60;
	int km_2 = 80;
	int km_3 = 100;
	int km_4 = 12;
	
	float mile_1 = km_1*mile;
	float mile_2 = km_2*mile;
	float mile_3 = km_3*mile;
	float mile_4 = km_4*mile;
	
	printf("%dkm는 %fmil과 같습니다.\n", km_1, mile_1);
	printf("%dkm는 %fmil과 같습니다.\n", km_2, mile_2);
	printf("%dkm는 %fmil과 같습니다.\n", km_3, mile_3);
	printf("%dkm는 %fmil과 같습니다.\n", km_4, mile_4);
	 
}
