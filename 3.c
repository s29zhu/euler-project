#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

#define N 600851475143

typedef struct node{
	long prime;
	struct node *link;
}primeLink;

bool  prime(primeLink *header, unsigned long prime);
unsigned long  factor(unsigned long factor, unsigned long residuePre);

int  main(int argc, char **argv){
	unsigned long i = 0;
	unsigned long maxFactor = 0;
	unsigned long residuePre = N;
	unsigned long residueAft = 0;
	unsigned long sqroot = 0;
	sqroot = floor(sqrt(N));
	primeLink *header = NULL;
	primeLink *tailor = header;
	primeLink *num = (primeLink *)malloc(sizeof(primeLink));
	header = num;
	num->prime = 2;
	num->link = NULL;
	tailor = num;
	residueAft = factor(num->prime, residuePre);
	if(residuePre != residueAft){
		residuePre = residueAft;
		maxFactor = num->prime;
	}
	printf("The square root of N is %lf \n", floor(sqrt(N)));
	for(i = 3; i < sqroot; i++ ){
		if(prime(header, i)){
			num = (primeLink *)malloc(sizeof(primeLink));
			num->prime = i;
			num->link = NULL;
			tailor->link = num;
			tailor = num;
			residueAft = factor(i, residuePre);
			if(residuePre != residueAft && residueAft != 0){
				maxFactor = num->prime;
				residuePre = residueAft;
				if(residuePre <= num->prime)
					break;
			}
		}
	}
	printf("the maximum prime factor %lu,  %lu\n", maxFactor, residuePre);
	return 1;
}

bool prime(primeLink *header, unsigned long prime){
	bool isPrime = true;
	bool notPrime = false;
	unsigned long sqroot = 0;
	sqroot = floor(sqrt(prime));
	primeLink *p = header;
	while(p && (p->prime <= sqroot)){
		if(prime % p->prime)
			p = p->link;
		else
			return notPrime;		
	}
	return isPrime;	
}

unsigned long  factor(unsigned long factor, unsigned long residuePre){
	int modRes = 0;
	if(residuePre < factor)
		return 0;
	modRes = residuePre % factor;
	if(!modRes)
		residuePre /= factor;
	return residuePre;
}
