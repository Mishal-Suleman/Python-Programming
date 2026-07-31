#include<stdio.h>
void main(){
    int a;
    printf("Enter your number: ");
    scanf("%d" , &a);
    if (a%2==0){
        printf("this is EVEN");
    }
    else 
        printf("this is ODD");

}