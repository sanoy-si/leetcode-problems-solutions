
from sys import setrecursionlimit, stdin
import threading
from bisect import bisect_right

def input():
    return stdin.readline().strip()

def int_list():
    return list(map(int,stdin.readline().strip().split()))

def main():
    n = int(input())
    shops = int_list()
    shops.sort()

    q = int(input())
    for _ in range(q):
        money = int(input())
        print(bisect_right(shops, money))

    
if __name__ == '__main__':
    
    setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()