#include <stdio.h>
#include <sys/time.h>


// piece positions increase in a clockwise direction
//
//

void render();

int board_fill[21] = {0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b100000000001,0b111111111111,};

typedef struct Shape
{
 int pos[4];
// int cPosVal
// int cPos[4];
}Shape;

void rotateShape();

void printScreen();

void init_q(Shape* shape, int pos)
{
	shape->pos[0] = 0b0000000000;
	shape->pos[1] = 0b0000000000;
	shape->pos[2] = 0b0000110000;
	shape->pos[3] = 0b0000110000;
}

void init_i(Shape* shape, int pos)
{
	if(pos==0||pos==2)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000000000;
		shape->pos[2] = 0b0001111000;
		shape->pos[3] = 0b0000000000;
	}
	else
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000010000;
		shape->pos[2] = 0b0000010000;
		shape->pos[3] = 0b0000000000;
	}
}

void init_z(Shape* shape, int pos)
{
	if(pos==0||pos==2)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000000000;
		shape->pos[2] = 0b0001100000;
		shape->pos[3] = 0b0000110000;
	}	
	else
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0001100000;
		shape->pos[3] = 0b0001000000;
	}
}

void init_t(Shape* shape, int pos)
{
	if(pos==0)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000000000;
		shape->pos[2] = 0b0001110000;
		shape->pos[3] = 0b0000100000;
	}	
	else if(pos==1)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0001100000;
		shape->pos[3] = 0b0000100000;
	}
	else if(pos==2)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0001110000;
		shape->pos[3] = 0b0000000000;
	}	
	else
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0000110000;
		shape->pos[3] = 0b0000100000;
	}
}

void init_s(Shape* shape, int pos)
{
	if(pos==0||pos==2)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000000000;
		shape->pos[2] = 0b0000110000;
		shape->pos[3] = 0b0001100000;
	}	
	else
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0000110000;
		shape->pos[3] = 0b0000010000;
	}
}

void init_j(Shape* shape, int pos)
{
	if(pos==0)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000000000;
		shape->pos[2] = 0b0001110000;
		shape->pos[3] = 0b0000010000;
	}	
	else if(pos==1)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0000100000;
		shape->pos[3] = 0b0001100000;
	}
	else if(pos==2)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0001000000;
		shape->pos[2] = 0b0001110000;
		shape->pos[3] = 0b0000000000;
	}	
	else
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000110000;
		shape->pos[2] = 0b0000100000;
		shape->pos[3] = 0b0000100000;
	}
}

void init_l(Shape* shape, int pos)
{
	if(pos==0)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000000000;
		shape->pos[2] = 0b0001110000;
		shape->pos[3] = 0b0001000000;
	}	
	else if(pos==1)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0001100000;
		shape->pos[2] = 0b0000100000;
		shape->pos[3] = 0b0000100000;
	}
	else if(pos==2)
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000010000;
		shape->pos[2] = 0b0001110000;
		shape->pos[3] = 0b0000000000;
	}	
	else
	{
		shape->pos[0] = 0b0000000000;
		shape->pos[1] = 0b0000100000;
		shape->pos[2] = 0b0000100000;
		shape->pos[3] = 0b0000110000;
	}
}

int main()
{
	struct timeval current_time;
	struct timeval begin;
	gettimeofday(&begin, NULL);

//	for(;;)
//	{
//		gettimeofday(&current_time,NULL);
//		if(current_time.tv_sec == begin.tv_sec)
//		{
//			printf("\n");
//		}
//	
//	}
//	printf("%c%c\n%c%c\n", 254,254,254,254);
//	printf("%c%c%c%c",219,219,219,219);
//	printf("\n    %c\n",219);
	
	Shape s;
	render(&s);
}

void printScreen(Shape* s)
{
	init_l(s,0);
	int i;
	int j;
	for(i=0;i<20;i++)
	{
		for(j=0;j<10;j++)
		{
			printf("%c%c",((s->pos[i%4]>>(9-j))&1) ? '[' : ' ',((s->pos[i%4]>>(9-j))&1) ? ']' : ' ');
		}
		printf("\n");
	}
}

void render(Shape* s)
{
	system("cls");
	printScreen(s);
}
