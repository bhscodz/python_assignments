#include <bits/stdc++.h>
using namespace std;
int max_sub(vector<int> arr,int k){
    int left=0,right=0,sum=0,max_length=0;
    while(sum<k && right==arr.size()){
        if(sum>k){
            sum-=arr[left];
            left++;
        }
        else{
            sum+=arr[right];
            right++;
        }
        if(sum==k){
            max_length=max(max_length,right-left+1);
        }
    }
    return max_length;
}
int main(){
    vector <int>arr={10,5,2,7,1};
    cout<<max_sub(arr,15);
    return 0;
}