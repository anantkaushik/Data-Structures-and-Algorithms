/*
// Sample code to perform I/O:

#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;										// Reading input from STDIN
	cout << "Input number is " << num << endl;		// Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    long long int flag=0,i;
    //scanf("%s",b);
    cin>>s;
    for(i=0;i<s.length();i++)
    {
        if(s[i]==s[i+1]&&s[i+1]==s[i+2]&&s[i+2]==s[i+3]&&s[i+3]==s[i+4]&&s[i+4]==s[i+5])
        {
            flag=1;
            break;       
        }
     
    }
    if(flag==1)
    cout<<"Sorry, sorry!";
    if(flag==0)
    cout<<"Good luck!";
    return 0;
}
    
        
