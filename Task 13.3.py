def bin_sys(a: int, b: int):
    for i in range(a, b+1):
        print(bin(i)[2::])
    print(bin(sum([i for i in range(a, b+1)]))[2::])
