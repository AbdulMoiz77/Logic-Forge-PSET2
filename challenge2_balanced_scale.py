def putStone(A, B, arr, stone_idx, target):
    if stone_idx == len(arr):
        return A == target and B == target

    # putting in bag A
    resA = False  
    if A + arr[stone_idx] <= target:
        resA = putStone(A+arr[stone_idx], B, arr, stone_idx+1, target)

    # putting in bag B
    resB = False
    if B + arr[stone_idx] <= target:
        resB = putStone(A, B+arr[stone_idx], arr, stone_idx+1, target)

    return resA or resB

def can_balance_scales(arr):
    total = sum(arr)

    if total % 2 :
        return False
    
    target = total // 2

    return putStone(0, 0, arr, 0, target)        

if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    print(can_balance_scales(arr))

    arr = [1, 3, 5]
    print(can_balance_scales(arr))