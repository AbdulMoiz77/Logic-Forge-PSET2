def can_balance_scales(arr):
    total = sum(arr)

    if total % 2 :
        return False
    
    target = total // 2

    sums = set()
    sums.add(0)

    for i in arr:        
        sumsCopy = sums.copy()
        for j in sums:
            if i + j == target:
                return True            
            elif i + j < target:
                sumsCopy.add(i+j)
        
        sums = sumsCopy

    return False       

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(can_balance_scales(arr))

    arr = [1, 3, 5]
    print(can_balance_scales(arr))