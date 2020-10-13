parking_lot = set()

count = int(input())

for i in range(count):
    (command, car) = input().split(', ')
    if command == 'IN':
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    [print(remaining_cars) for remaining_cars in parking_lot]
else:
    print('Parking Lot is Empty')
