strings = ['a', 'b', 'c', 'd']

# Push -> O(1)
strings.append('e')
# Pop -> O(1)
strings.pop()
strings.pop()
# Insert at first position -> unshift -> O(n)
strings.insert(0, 'x') 
# Insert at position -> splice -> O(n)
strings.insert(2, 'f')

print(strings)

