#include <stdio.h>

int main(){
	
	float x;
	float y;
	char ans;
	
	while (true){	
		printf("\nx�� ���� �Է��Ͻÿ�:");
		scanf("%f", &x);
	
		if (x<=0){
			y = x*x - 9*x +2;
		}
		else{
			y = 7*x +2;
		}
	
		printf("f(x)�� ���� %f\n", y);
		
		
		printf("��� ����� �����ұ��?");
		scanf("%c", &ans);
		
		if (ans == 'y'){
			continue;
		}
		else{
			break;
		}
		
	}

}
