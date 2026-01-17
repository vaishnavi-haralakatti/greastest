import sys

def greatest(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
    except IndexError:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))

    print("Greatest:", greatest(a, b, c))

