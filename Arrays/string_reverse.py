print('eispoohw'[::-1])

# or

def reverse(str):
    r_str = []
    total = len(str) - 1

    for i in range(total, -1, -1):
        r_str.append(str[i])

    return ''.join(r_str)

print(reverse('whoopsie'))
    
