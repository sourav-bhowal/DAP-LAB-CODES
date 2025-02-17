def unique_elements(lst):
    return list(set(lst))

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Unique elements:", unique_elements(lst))
