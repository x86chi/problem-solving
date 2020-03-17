# coding : utf-8

def k_right_rotate(arr: int, s: int, t: int, k: int) :
    last = []
    for i in range(t, t - k, -1):
        last.append(arr[i])
    for i in range(t, t - k - 1, -1):
        arr[i] = arr[i - k]
    for i, atom in enumerate(reversed(last)):
        arr[s + i] = atom
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(k_right_rotate(arr, 2, 6, 2))
