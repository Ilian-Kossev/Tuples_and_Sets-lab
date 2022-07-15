ll = [2, 3, 5, 6, 5, 8, 2, 6, 9]
target = 17
index = 0
target_found = False
while True:
    for num in range(index, len(ll)):
        if ll[index] + ll[num] == target:
            print(ll[index], ll[num])
            target_found = True
            break
    if target_found:
        break
    index += 1
