def mountainPeak(n):    
    if n < 1 or n > 45:
        return 0  

    if n == 1:
        return 1

    # fibonacci series
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c

    return b

if __name__ == "__main__":
    print(mountainPeak(4))