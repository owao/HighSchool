#include <stdio.h>

int main(){
	
	long long S_to_M = 1179000000; //km, Sun to Mars
	long long S_to_U = 2871000000; //km, Sun to Uranus
	
	long long M_to_U = S_to_U - S_to_M;
	
	printf("ȭ���� õ�ռ� ���� �Ÿ��� %lldkm�Դϴ�.", M_to_U); 
	
}
