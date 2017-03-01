def test_num(a,b):
    return a+b


def test_remove(a, b):
    if a>0:
        a = 10
    if b<0:
        b = 10
    return a + b

if __name__ == '__main__':
    test_num(5, 6)
    test_remove(5, 6)