#include <stdio.h>

int main(){	

	int N;
	scanf("%d", &N);
	
	for(int i=-N+1; i<=N-1; i++){
		for(int j=-N+1; j<=N-1; j++){
			
			int ii = (i>0)? N-i : i+N;
			int jj = (j>0)? N-j : j+N;			
			
			if (jj>ii) printf(" ");
			else printf("%d", jj);
		}
		printf("\n");
	}
}
