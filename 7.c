#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define N 10001

bool prime(unsigned long *array, unsigned long num){
	unsigned long sqroot = 0;
	int i = 0;

	sqroot = floor(sqrt(num));
	for(i = 0; array[i] <= sqroot; i++ ){
		if( num % array[i] == 0) 
				return false;
	}
	return true;
}

int main(int argc, char **argv){
	unsigned long array[N]={0};
	unsigned long num = 2;
	int i = 0;
	array[i] = 2;
	while(i != N-1){
		num++;
		if(prime(array, num)){
			i++;
			array[i] = num;
		}	
	}
	printf("The 10001st prime number is %.lu\n", array[i]);
}
