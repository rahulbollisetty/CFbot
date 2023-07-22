#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
 
#define ff              first
#define ss              second
#define int             long long
#define pb              push_back
#define mp              make_pair
#define pii             pair<int,int>
#define vi              vector<int>
#define mii             map<int,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define setbits(x)      __builtin_popcountll(x)
#define zrobits(x)      __builtin_ctzll(x)
#define mod             1000000007
#define inf             1e18
#define ps(x,y)         fixed<<setprecision(y)<<x
#define mk(arr,n,type)  type *arr=new type[n];
#define w(x)            int x; cin>>x; while(x--)
#define FOR(x,a,b) for(int x=a;x<b;x++) 
#define FORR(x,arr) for(auto& x:arr)
#define OSTREAM(...)    ;
#define OSTREAM0(...)   ;
#define ALL(a) (a.begin()),(a.end())
mt19937                 rng(chrono::steady_clock::now().time_since_epoch().count());
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
template<typename T>             istream& operator>>(istream& is,  vector<T> &v){for (auto& i : v) is >> i;        return is;}
template<typename T>             ostream& operator<<(ostream& os,  vector<T>  v){for (auto& i : v) os << i << ' '; return os;}
template<typename T>             vector<T>& operator--            (vector<T> &v){for (auto& i : v) --i;            return  v;}
template<typename T>             vector<T>& operator++            (vector<T> &v){for (auto& i : v) ++i;            return  v;}
int n;
void solve()
{
  //  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
//   cin>>n;
vi v(2);
cin >> v;
--v;
cout<<v;
cout<<endl;
}
 
int32_t main()
{
    //make sure to comment the lines below before submitting it to the online judge
    #ifndef ONLINE_JUDGE 
    // Change the input0.txt according to the number of files
    // For getting input from input0.txt file 
    freopen("input0.txt", "r", stdin); 
    #endif
    // Your code goes here
int t;
cin>>t;
while(t--)
    solve();
    return 0;
}