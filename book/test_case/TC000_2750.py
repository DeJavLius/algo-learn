import numpy as np

def TC_001():
    N = 1
    print(str(N))
    for n in list(np.random.choice(range(1, N + 1), N, replace=False)):
        print(n)

TC_001()

def TC_002():
    N = 5
    print(str(N))
    for n in list(np.random.choice(range(1, N + 1), N, replace=False)):
        print(n)

TC_002()

def TC_003():
    N = 100
    print(str(N))
    for n in list(np.random.choice(range(1, N + 1), N, replace=False)):
        print(n)

TC_003()

def TC_004():
    N = 1000000
    print(str(N))
    for n in list(np.random.choice(range(1, N + 1), N, replace=False)):
        print(n)

TC_004()