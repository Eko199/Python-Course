def is_valid_UCN(ucn, *, bypass_checksum = False):
    month = int(ucn[2] + ucn[3])

    if month < 1 or 12 < month < 21 or 32 < month < 41 or month > 52:
        return False
    
    if bypass_checksum:
        return True

    weights = 2, 4, 8, 5, 10, 9, 7, 3, 6
    sum = 0

    for i in range(9):
        sum += int(ucn[i]) * weights[i]

    return int(ucn[9]) == sum % 11 if sum % 11 < 10 else int(ucn[9]) == 0

print(is_valid_UCN("6101057509") == True)
print(is_valid_UCN("6101057500", bypass_checksum=True) == True)
print(is_valid_UCN("6101057500") == False)
print(is_valid_UCN("6913136669") == False)