#include<iostream>
#include<stdlib.h>
#include<vector>
#include "fill_tetrahedron.cpp"
using namespace std;

void merge(int* arr, int leftSize, int size)
{
    vector<int> tmp;
    int currElem=0;
    int curr = leftSize;
    size = leftSize+size;
    while(currElem<leftSize && curr < size)
    {
        if(arr[currElem] < arr[curr])
        {
            tmp.push_back(arr[currElem]);
            currElem++;
        }
        else
        {
            tmp.push_back(arr[curr]);
            curr++;
        }
    }
    if(currElem<leftSize)
    {
        while(currElem<leftSize)
        {
            tmp.push_back(arr[currElem]);
            currElem++;
        }
    }
    else if(curr<size)
    {
        while(curr<size)
        {
            tmp.push_back(arr[curr]);
            curr++;
        }
    }
    int sz = tmp.size();
    for(int i=0;i<sz;i++)
    arr[i]=tmp[i];
}

void mergeSort(int* arr, int size)
{
    if (size <= 2)
    {
        if (size == 2)
        {
            if (arr[0] > arr[1])
                {
                swap(arr[0], arr[1]);
                }
        }
    return;
    }
    mergeSort(arr, size / 2);
    mergeSort(arr + size / 2, (size + 1) / 2);
    merge(arr, size / 2, (size + 1) / 2);
}
int tetrahedron_filled(int* arr, int val)
{
    int sz=0;
    while(arr[sz])
        sz++;
    mergeSort(arr,sz);
    int cnt=0;
    float cost=0;
    float valueLitres = val;
    for(int i=0;i<sz;i++)
    {
        cost = fill_tetrahedron(arr[i]);
        if(cost<=valueLitres)
        {
            valueLitres-= cost;
            cnt++;
        }
        else
            break;
    }
    return cnt;

}

