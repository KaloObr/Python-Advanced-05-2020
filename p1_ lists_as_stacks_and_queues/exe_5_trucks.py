from collections import deque

n = int(input())
gas_stations = deque()

for _ in range(n):
    pump = [int(x) for x in input().split()]
    gas_stations.append(pump)

for index in range(n):
    is_valid = True
    fuel = 0

    for _ in range(n):
        current = gas_stations.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        gas_stations.append(current)

    if is_valid:
        print(index)
        break

    gas_stations.append(gas_stations.popleft())
