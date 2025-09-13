import argparse
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N', type=int, default=10)
    args, _ = parser.parse_known_args()

    arr = [random.randint(1, 100) for _ in range(args.N)]
    print(' '.join(str(x) for x in arr))
    bubble_sort(arr)
    print(' '.join(str(x) for x in arr))

if __name__ == '__main__':
    main()
