#include<stdio.h>

/*
Runtime: 56 ms, faster than 80.79% of C online submissions for Jump Game.
Memory Usage: 8.2 MB, less than 74.83% of C online submissions for Jump Game.
*/

bool tuantuan(int s[], int n) 
{
	int i;
	int zero = -1;
	for(i = n - 1; i >= 0; i--)
	{
		if(s[i] == 0 && zero == -1) zero = i;
		if(s[i] == 0 && i == n - 1)
 	  	{
 	  	    if((zero != -1) && s[i]> (zero - i - 1)) zero = -1;
 	  	}
	  	else
	  	{
		    if((zero != -1) && s[i]> (zero - i)) zero = -1;
	 	}
	}
	if(zero == -1) return true;
	else return false;
}

int main ()
{
	 int n = 12;
	 int s[12] = {5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0};
	if (tuantuan(s, n))	printf("True\n");
	else printf("False\n");
	return 0;
}
