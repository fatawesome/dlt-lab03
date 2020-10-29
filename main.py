def task1(x, y, a):
    s = (3 * x ** 2 + a) // (2 * y)
    x2 = s ** 2 - 2 * x
    y2 = s * (x - x2) - y
    return x2, y2

print(task1(2, 3, 0))

def task2_helper(a, b, p):
    for x in range(p):
        for y in range(p):
            if y ** 2 % p == (x ** 3 + a * x + b) % p:
                yield x, y

def task2(a, b, p):
    return list(task2_helper(a, b, p))[:100]
            
print(task2(5, 7, 107))


_3_ = list
def task3_2(a, b, p):
    import matplotlib.pyplot as _4_
    _1_ = task2(a, b, p)
    _2_ = _3_(zip(*_1_))
    _4_.scatter(*_2_)
    _4_.show()

task3_2(5, 7, 101)
