
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <time.h>

void delay();
void printField();
int checkInput(char c);

void render(char* ptr){
	system("clear");
	printField(ptr);
	delay();
}

int main(){
	char ch = 'a';
	char field[110] = {'.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n',
			   '.','.','.','.','.','.','.','.','.','.','\n'};

	char* ptrField = &field;
	char x;
	int y = 1;
	while(y){
		render(ptrField);
		ptrField = &field;
		x = getchar();
		getchar();
		if(x=='q'){
			y=0;
		}
		//checkInput(ch);
	}
	printf("Game over..");
}

void printField(char* ptr){
	int i=0;
	for(i=0;i<110;i++){
		printf("%c",*(ptr));
		ptr++;
	}
}

int checkInput(char ch){
	int x;
	switch(ch){
		case 'w':	x=0;
			break;
		case 'a':x=0;
			break;
		case 's':x=0;
			break;
		case 'd':x=0;	
			break;
		default:x=1;
			break;
	
	}
	return x;
}

void delay(){
	int i=0;
	int x=0;
	for(i=0;i<10000;i++){
		x=i;
	}
}
