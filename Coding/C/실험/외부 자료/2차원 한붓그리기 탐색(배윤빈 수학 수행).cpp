#include<stdio.h>
int search(int x, int y, int depth)
{
	int cnt=0;
	if ((x<0)||(w<=x)||(y<0)||(h<=y))
		return 0;
	if ((map&(1<<(x+y*w)))>0)
		return 0;
	if (depth==w*h)
		return 1;
	map += 1 << (x+y*w);
	cnt = cnt + search(x+1, y, depth+1);
	cnt = cnt + search(x-1, y, depth+1);
	cnt = cnt + search(x, y+1, depth+1);
	cnt = cnt + search(x, y-1, depth+1);
	map -= 1<< (x+y*w);
	return cnt;
}
	
int main(void)
{	
	int map = 0;

	int w;
	int h;
	
	printf("Enter width : ");
	scanf("%d", &w);
	printf("Enter height : ");
	scanf("%d", &h);
	
	printf("Your map vv \n");
	
	int k;
	int l;
	for (l=1;l<=h;l++)
	{
		for (k=1;k<=w;k++)
		{
			printf(". ");
		}
		printf("\n");
	}
	
	printf("\n");
	int m;
	for (m=1;m<=w;m++)
	{
		printf("==");
	}
	printf("\n");
	
	int count = 0;
	int i;
	for (i=0; i<w*h; i++)
	{
		count = count + search(i%w, i/w, 1);
	}
	printf("Number of cases : %d", count/2);
	return 0;
