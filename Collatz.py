#collatz program. function that eventually returns a 1 given any integer given certain rules

#if num is even divide by 2. // is integer division. / is floating point
#otherwise multiply by 3 and add 1
def collatz(numCollatz):
    if numCollatz % 2 == 0:
        numCollatz = numCollatz // 2
    else:
        numCollatz = 3 * numCollatz + 1
    return numCollatz;

#type cast the input to an integer so that it will work
num = int(input("Enter a number "));

#while num given doesnt equal 1 keep calling collatz function
while num != 1:
    if num == 0:
        print("Does not work for 0") #will not work for 0 
        break
    else:
        num = collatz(num)
    print(num)
