#include <ncurses.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

bool delay(clock_t *st, int *fs, bool *b){
	clock_t c = clock();
	*b = ((c - *st + *fs) > 0 ? false : true);
}

int main(){
	bool b = false;
	bool *bp = &b;
	clock_t start_time = clock();
	clock_t *st = &start_time;
	int fall_speed = 10000;
	int *fs = &fall_speed;
	delay(st,fs,bp);
	char hello[6]="hello";
	int x=1;
	int y=1;
	// initialisation
	initscr();
	noecho();
	cbreak();

	mvprintw(y,x,hello);
	refresh();
	while(1){
		delay(st,fs,bp);
		if(*bp){
			*bp=false;
			start_time=clock();
			y--;
			mvprintw(y,x,hello);
			refresh();
		}	
	}
	// waits for character input
	//getch();
	// closes ncurses screen
	endwin();

	return 0;
}


