#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 50

enum type {KPOP = 1, DANCE, HIPHOP, ROCK};
char *genreName[] = {"", "KPOP", "DANCE", "HIPHOP", "ROCK"};

struct Music{
	char singer[SIZE];
	char title[SIZE];
	enum type genre;
};

void menu(){
	printf("====================\n");
	printf(" 1. Add\n");
	printf(" 2. Print\n");
	printf(" 3. Search\n");
	printf(" 4. Exit\n");
	printf("====================\n");
}

int getMenu(){
	int a;
	printf("Input Menu Num : ");
	scanf("%d", &a);
	return a;
}

void addMusic(struct Music M[SIZE], int mCount){
	printf("Singer : ");
	scanf("%s", &M[mCount].singer);
	printf("Title : ");
	scanf("%s", &M[mCount].title);
	printf("Genre(1: KPOP, 2: DANCE, 3: HIPHOP, 4: ROCK) : ");
	scanf("%d\n", &M[mCount].genre);
}

void printMusic(struct Music M[SIZE], int mCount){
	for(int i=0; i<mCount; i++){
		printf("Singer : %s, Title : %s, Genre : %s\n", M[i].singer, M[i].title, genreName[M[i].genre]);
	}
}

void searchMusic(struct Music M[SIZE], int mCount){
	char name[SIZE];
	printf("Title : ");
	scanf("%s", name);
	for(int i=0; i<mCount; i++){
		if(strcmp(M[i].title, name)==0){
			printf("%s\n", M[i].singer);
			break;
		}
	} 
}

int main(void){
	
	Music M[SIZE];
	int num, mCount=0;
	
	while(true){
		menu();
		num = getMenu();
		switch(num){
			case 1:
				addMusic(M, mCount);
				mCount++;
				continue;
			case 2:
				printMusic(M, mCount);
				continue;
			case 3:
				searchMusic(M, mCount);
				continue;
			case 4:
				break;
		}
		break;
	}
	
	return 0; 
} 
