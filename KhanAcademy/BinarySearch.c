#include <stdio.h>

int BnrSrch (int SizeOfArray, int target, int arr[]);



int main(int argc, char const *argv[])
{
	
	int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

	// Determine de Size of an array in C
	int SizeArr = sizeof(primes)/sizeof(primes[0]);

	/* BluePrint : To determine what the size of the array
	 printf("The size of the array is %d\n", SizeArr); */

	int result = BnrSrch( SizeArr, 73,primes);
	printf("The index of the number is number %d\n", result);
		return 0;
}


int BnrSrch(int SizeOfArray, int target, int arr[]){

	int min = 0;
	int max = SizeOfArray - 1;
	int walker;

	while ( max>=min){

		walker = (max + min)/2;
		if (arr[walker]== target)
		{
			return walker;
		}
		else if (arr[walker]<target)
		{
			min = walker -1;
		}
		else
		{
			max = walker -1;
		}


	}
	
}