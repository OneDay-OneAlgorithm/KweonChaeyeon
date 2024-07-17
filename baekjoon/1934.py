import sys

def GCD(a, b):
    if (b == 0):
        return a
    
    return GCD(b, a % b)

def main():
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        a, b = map(int, input().split())
        
        g = GCD(a, b)
        print(a * b // g)

if __name__ == "__main__":
    main()