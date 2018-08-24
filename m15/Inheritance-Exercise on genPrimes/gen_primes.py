#define the gen_primes function here
def genPrimes():
    nxt = 2
    while True:
        c_v = 0
        for n in range(1, nxt+1):
            if nxt % n == 0 & c_v<4:
                c_v += 1
        if c_v == 2:
            yield nxt
            nxt += 1
        else:
            nxt += 1

def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = genPrimes()
    for i in range(a):
        p = primeGenerator.__next__()
        if(i%b == 0):
            print(p)

if __name__ == "__main__":
    main()
