if __name__ == "__main__":
    n = int(input())
    if n == 2:
        print(1)
        print(2)
    elif n == 1:
        print(1)
        print(1)
    else:
        addend = [1]
        n -= 1
        while True:
            add_next = addend[-1] + 1
            if n - add_next == 0:
                addend.append(add_next)
                break
            if (n - add_next) > add_next:
                addend.append(add_next)
                n -= add_next
            else:
                addend.append(n)
                break
        print(len(addend))
        [print(i, end=' ') for i in addend]
