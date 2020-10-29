def ec2p(x, y, a):
    s = (3 * x ** 2 + a) // (2 * y)
    x2 = s ** 2 - 2 * x
    y2 = s * (x - x2) - y
    return x2, y2

print(ec2p(2, 3, 0))