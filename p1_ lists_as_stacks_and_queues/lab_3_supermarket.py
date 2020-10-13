from collections import deque


def solve():
    q = deque()
    while True:
        command = input()
        if command == "End":
            print(f'{len(q)} people remaining.')
            break
        elif command == "Paid":
            while q:
                print(q.popleft())
        else:
            q.append(command)


solve()

