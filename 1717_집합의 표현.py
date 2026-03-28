#include <iostream>
#include <vector>
#include <numeric>

using namespace std;
int find(int x , vector<int> &parents){
	if (x!=parents[x]){
		parents[x]=find(parents[x],parents);
	}
	return parents[x];
}



void union1(int a,int b,vector<int> &parents){
	a=find(a,parents);
	b=find(b,parents);
	if (a<b){
		parents[b]=a;
	}
	else if (a>b){
		parents[a]=b;
	}

}


int main(){
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n,m;
	cin >> n;
	cin >> m;
	vector<vector<int>>li2(n+1,vector<int>(n+1)); // 연결행렬
	for (int i=1; i<=n; i++){
		for (int j=1; j<=n; j++){
			cin >> li2[i][j];
		}
	}
	
	vector<int>ar2(n+1,0);
	for (int i=1; i<=m; i++){
		int trip;
		cin >> trip;
		ar2[trip]=2;
	}

	vector<int>parents(n+1);
	for (int i=1; i<=n; i++){
		parents[i]=i; // 처음 상태
	}

	for (int i=1; i<=n; i++){
		for (int j=1; j<=n; j++){
			if (li2[i][j]==1){
				union1(i,j,parents);
			}
		}
	}

	
	vector<int>ar10;
	
	for (int i=1; i<=n; i++){
		if (ar2[i]==2){
			ar10.push_back(i);
		}
	}
	string ans="YES";
	for (size_t i=0; i<ar10.size()-1; i++){
		if (find(ar10[i],parents)!=find(ar10[i+1],parents)){
			ans="NO";
			break;
		}
	}
	cout << ans;
	return 0;
}
