#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	
	int A;
	int B;
	int num = 0; //�Ҽ� ����
	int sum = 0; //�Ҽ� �� 
	int count = 1; //�ӽ� ���� 
	
	scanf("%d %d", &A, &B);
	
	for(int i=A; i<B+1; i++){
		if(i==1 || (i>2 && i%2==0)){ //1�̰ų� ¦���� �Ÿ��� 
			continue;
		}
		 for(int j=2; j<i; j++){ //�������� ���� �ִ��� �˻��Ѵ� 
		 	if(i%j==0){
		 		count=0;
			 }
		}
		if(count){
			num += 1;
			sum += i;
		}
		count = 1; //�ʱ�ȭ 
	}
	
	printf("%d %d", num, sum);
	
	return 0;
}
