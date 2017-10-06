#collatz program. function that eventually returns a 1 given any integer given certain rules

def collatz(numCollatz):
    if numCollatz % 2 == 0:
        numCollatz = numCollatz // 2
    else:
        numCollatz = 3 * numCollatz + 1
    return numCollatz;

num = int(input("Enter a number  "));

while num != 1:
    num = collatz(num)
    print(num)
