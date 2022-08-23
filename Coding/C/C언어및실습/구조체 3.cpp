#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student{
	int num; //ÇÐ¹ø 
	char name[10];
	float grade;
};

void inputStudents(struct Student a[3]){
	for(int i=0; i<3; i++){
		scanf("%d %s %f", &a[i].num, &a[i].name, &a[i].grade);
	}
}

void findByName(struct Student a[3]){
	char Name[10];
	scanf("%s", &Name);
	
	for(int i=0; i<3; i++){
		if(strcmp(a[i].name, Name)==0){
			printf("%d %s %f\n", a[i].num, a[i].name, a[i].grade);
		}
	}
}

void findByScore(struct Student a[3]){
	float Grade;
	scanf("%f", &Grade);
	
	for(int i=0; i<3; i++){
		if(a[i].grade >= Grade){
			printf("%d %s %f\n", a[i].num, a[i].name, a[i].grade);
		}
	}
}

int main(void){
	
	struct Student a[3];
	
	inputStudents(a);
	
	findByName(a);
	findByScore(a);

	return 0; 
} 
