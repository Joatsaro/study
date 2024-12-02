print("Hello")

# Given a list of nested lists. Return a "flattened" list, e.g.
# [10, [11, [12]]] -> [10, 11, 12]
final_list = []
initial_list = [10, [11, [12, [13, [14]]]]]
ini = initial_list
x = 1
while x == 1:
    for i in ini: # lets iterate through list
        if type(i) is list:
            ini = i # if the i type is a list, we must now iterate on it
            break  # Break the previous for and jump to a new one with our new ini variable
        else:  # if the 10 is not a list it will just append it to final list
            final_list.append(i)
            if len(ini) == 1:
                x = 0  # If len == 1 it means there is no more need for iterating, we reached the end
    continue  # Lets go back to the while with our new ini variables
print(final_list)
