# include <stdio.h>

void left_rotate(int arr[], int s, int t)
{
    int i, first;
    first = arr[s];
    for (i = s; i < t; i++)
        arr[i] = arr[i + 1];
    arr[t] = first;
    return arr;
}

void k_right_rotate(int arr[], int s, int t, int k)
{
    int i, last[k];
    int move_last = t - k;
    for (i = t; i > move_last; i--)
        last[t - i] = arr[i];
    for (i = t; i > move_last - 1; i--)
        arr[i] = arr[i - k];
    for (i = 0; i < k; i++)
        arr[s + i] = last[k - 1 - i];
    return arr;
}

void print_arr(int arr[], int arr_len)
{
    for (int i = 0; i < arr_len; i++)
        print('%d \n', arr[i]);
}

#define N 10

int main()
{
    int a[N], i;

    for (i = 0; i < N; i++)
        a[i] = i;
    // left_rotate(arr_left, 2, 6);

    k_right_rotate(a, 2, 6, 2);
    print_arr(a, N);
}
