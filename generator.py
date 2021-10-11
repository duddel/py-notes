def collatz(n):
    i = n
    while i > 1:
        yield int(i)
        if i % 2 == 0:
            i /= 2
        else:
            i = i*3+1
    yield 1

if __name__ == "__main__":
    for i in collatz(1234567):
        print(i)
