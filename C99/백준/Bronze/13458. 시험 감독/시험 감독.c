#include <stdio.h>
int arr[1000000];

int main(){
    int n,b,c;
    long long count=0;
    scanf("%d",&n);//시험장의 수
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);//각 시험장의 응시자 수
    }
    scanf("%d %d",&b,&c);
    for(int i=0;i<n;i++){
        if(arr[i]<=0){
            continue;
        }
        int temp=arr[i]-b;
        count+=1;
        if(temp>0){
            if(temp%c==0){
                count+=temp/c;
            }else{
                count+=temp/c+1;
            }
        }
    }
    printf("%lld",count);
}