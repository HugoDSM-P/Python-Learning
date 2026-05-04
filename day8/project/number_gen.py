c = 1

def text(generator):
    print("Hello, your turn is:")
    print(next(generator))
    print("Please wait for your turn.")


def fragrance(c):
    while True:
        yield f"F-{c}"
        c += 1

def cosmetics(c):
    while True:
        yield f"C-{c}"
        c += 1

def pharmacy(c):
    while True:
        yield f"P-{c}"
        c += 1