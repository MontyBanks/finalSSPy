#In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
    'return a list with the reverse order of l'
    return list(reversed(l))

print(reverse_list([1,2,3,4]))  #[4,3,2,1])
print(reverse_list([3,1,5,4]))  #[4,5,1,3])