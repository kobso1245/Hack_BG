#include<iostream>
#include<string>
using namespace std;

string caesar_encrypt(string str,int otmestvane)
{
    int sz = str.length();
    string outStr = str;
    int code;
    for(int i=0;i<sz;i++)
    {
        //namirame koda na bukvata
        if(str[i]-'a' >= 0)
        {
            //imame malka bukva
            code = str[i] - 'a';
            outStr[i] = (char)(((code + otmestvane)%26)+(int)'a');

        }
        else
        {
            //imame golqma bukva
            code = str[i] - 'A';
            outStr[i] = (char)(((code + otmestvane)%26)+(int)'A');
        }
    }
    return outStr;
}
