n = int(input())
parking_lot = set()
for num in range(n):
    command = input().split(', ')
    direction = command[0]
    car_num = command[1]
    if direction == 'IN':
        parking_lot.add(car_num)
    else:
        parking_lot.remove(car_num)
if len(parking_lot) > 0:
    [print(num) for num in parking_lot]
else:
    print(f'Parking Lot is Empty')

