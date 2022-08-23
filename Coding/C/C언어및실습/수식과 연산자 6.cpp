#include <stdio.h>

int main(){
	
	int H; //hour
	int M; //minute
	int time;
	
	scanf("%d %d\n%d", &H, &M, &time);
	
	H = (H + ((M+time)/60)) % 24;
	M = (M + time) % 60;
	
	printf("%d %d", H, M);
	
}
