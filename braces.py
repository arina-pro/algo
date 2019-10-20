def check_braces(s):
    stack = []
    stack_ind = []
    spar = ('[','(', '{')
    spar2 = (']',')','}')
    for ind, c in enumerate(s):
        if c in spar:
            stack.append(c)
            stack_ind.append(ind)
        elif c in spar2:
            if stack == []:
                return ind+1
            if stack.pop() + c in ('[]','()','{}'):
                stack_ind.pop()
                continue
            else:
                return ind + 1
        else:
            continue
    if stack != []:
        return stack_ind.pop() + 1
    return 'Success'

        
if __name__ == "__main__":
    s = str(input())
    print(check_braces(s))
