# Find the GCD of two positive integers using loops.

a = 24;
b = 76;
r = 1;

while r != 0:
    r = b%a
    if r == 0:
        print("GCD is : " , a);
        break;
    else:
        a = r
        b = a