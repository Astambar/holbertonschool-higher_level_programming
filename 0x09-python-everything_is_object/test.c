#include <stdio.h>
 
int main ()
{
	int numfiles = 28;
FILE *files[numfiles];
for (int i = 0; i <= numfiles; i++)
{
    char filename[30];
    sprintf(filename, "%d-answer.txt", i);
	if(!(files[i] = fopen(filename, "r"))){
		files[i] = fopen(filename, "w");
	}
}

return 0;
}
