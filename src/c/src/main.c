#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[])
{
	char arg2[64];
	puts("Minecraft Package Manager C Remake");
	switch(argc)
	{
		case 1:
			puts("Not enough args.");
			return 1;
		case 2:
			strcpy(arg2, argv[1]);
			if(strcmp(arg2, "install") == 0)
			{
				puts("Install!");
			}
	}
	return 0;
}
