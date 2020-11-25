#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

void fallCheck(time_t start, bool *b, int fs){
	if((start+fs)<time(NULL)){
		*b=true;
	}

}

int main(){
	bool b=false;

	time_t start,end;
	
	time(&start);
	volatile long unsigned i=0;
	for(i=0;i<5000000000;i++)
		;
	
	time(&end);
	printf("\n%f\n",difftime(end,start));
	
	return 1;
}
