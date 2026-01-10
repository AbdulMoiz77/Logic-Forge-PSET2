def mountainPeak(n, steps, l = None):    
    if n == 0:
        steps.append(l)
        return
    
    if n < 0 or n > 45:
        return    
    
    if l is None:
        l = []

    # taking 1 step
    mountainPeak(n-1, steps, l + [1])

    # taking 2 steps
    mountainPeak(n-2, steps, l + [2])
    

if __name__ == "__main__":
    steps = []
    mountainPeak(3, steps)
    print(len(steps), steps)