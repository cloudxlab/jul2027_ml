def my_square(x):
    print("Computing square")
    return x*x

def diff(f, x):
    print("Inside Diff")
    eps = 1e-8
    return (f(x+eps) - f(x))/eps

if __name__ == '__main__':
    print(my_square(4))
