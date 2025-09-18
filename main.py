def add(a, b):
    return a + b

def main():
    x = 1
    y = 2
    import pdb; pdb.set_trace()  # <- breakpoint as requested
    result = add(x, y)  # TypeError after you continue
    print("result:", result)

if __name__ == "__main__":
    main()
