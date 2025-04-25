#include <bits/stdc++.h>
using namespace std;
void reverse_arr(vector<int>&a,int start,int end){
    if(start==end||end<start) return ;
    swap(a[start],a[end]);
    reverse_arr(a,start+1,end-1);
    
}
int main(){
    vector<int> a={1,8,3,5,6,8,9,10};
    reverse_arr(a,0,a.size()-1);
    for(auto &ch:a){
        cout<<ch<<" ";
    }
    return 0;
}