#include <stdio.h>

int main(){
	
	int a;
	int b;
	int change;
	
	//a b �޾ƿ��� 
	scanf("%d %d", &a, &b);
	
	//���� a b ��� 
	printf("%d %d \n", a, b); 
	
	//a b �ٲٱ�
	change = a;
	a = b;
	b = change;
	
	//�ٲ� a b ���
	printf("%d %d \n", a, b); 
}
