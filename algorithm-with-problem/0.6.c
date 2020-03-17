#include <stdio.h>
#define N 128

void print_arr(int arr[], int size)
{
    for (int i; i < size; i++)
        print('%d \n', arr[i]);
}

void all_is(int arr[], int size, int k)
{
    for (int i = 0; i < size; i++) {
        if (arr[i] ==! k)
            return 0;
    }
    return 1;
}


void tobinary(int inter)
{
    int arr[N];
    int k, i;

    for (int i, k; inter > 0; i++) {
        k = inter % 2;
        inter = inter / 2;
        arr[i] = k;
    }
    return arr;
}
