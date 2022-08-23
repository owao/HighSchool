#include <stdio.h>
#include <math.h>

void squareNumber(int A, int B) {
	
	int Min=-1;
	int sum=0;
	
	for(int i=A; i<=B; i++){
		if (sqrt(i)==(int)sqrt(i)){
			sum += i;
			if(Min==-1){
				Min = i;
			}
		}
	}
	if(Min==-1){
		printf("-1");
	}
	else{
		printf("%d\n%d", sum, Min);
	}


}

int main() {
	
   int A, B;
   scanf("%d %d", &A, &B);
   squareNumber(A,B);

}
