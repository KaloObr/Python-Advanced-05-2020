# list
# Dynamic size
#   - grow
#   - shrink
#
# random element access
#   - first [0]
#   - middle [5]
#   - last [7], [-1]

# Stack
# one of the 3 linear data structures other being lists and queue
# The process of adding data to a stack is referred to as "push"
# Retrieving data from a stack is called a "pop"
# Dynamic size
#   - grow ( append (left))
#   - shrink (pop())
#
# element access at the end
#   - current element ([-1])
# Stack is used to put limitations in place

"""
s = []
s.append(3)
s.append(5)
s.append(7)
print(s)

while s:
    print(s.pop())
"""

# ==============================================================
# Queue
# a queue is a first in first out abstract data type
# Used quite a lot and more often than the Stack
# We want them when we want things to happen in the order they were called
# Used when processing a lot of information
#
# it can be done with a list but that would be slow
# q = []
# q.append(8)
# q.append(9)
#
# while q:
#   print(q[0])
#   q = q[1:]
#
# That's why we use the deque from collection so that we can
# pop them from the left side

from collections import deque

q = deque()

q.append("first")
q.append("second")
q.append("last")

while q:
    print(q.popleft())


# dvo svurzana opashka? - deque e tova ili double Q.
# imame opashka koqto moje da dobavqme i da trieme ot dvata kraq

q.appendleft('1')
q.appendleft('2')
q.appendleft('3')

while q:
    print(q.pop())
