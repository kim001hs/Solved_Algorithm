#include<stdio.h>
int main(){
    int a;
    scanf("%d",&a);
    int res=1;
    for(int i=0;i<a;i++){
        res*=2;
    }
    printf("%d",res);
}